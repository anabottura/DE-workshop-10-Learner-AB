import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import boto3
import os
import argparse

# Constants from environment variables (or default values)
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "default-bucket-name")
INITIAL_DATASET_KEY = os.getenv("INITIAL_DATASET_KEY", "data/Employee_Batch_0.csv")
WEEKLY_BATCH_KEYS = os.getenv("WEEKLY_BATCH_KEYS", "data/Employee_Batch_1.csv,data/Employee_Batch_2.csv")
OUTPUT_PREDICTIONS_KEY = os.getenv("OUTPUT_KEY", "output/attrition_predictions.csv")  # S3 key for predictions

def fetch_dataset(bucket_name, file_key):
    """
    Fetches a CSV file from an S3 bucket and returns it as a pandas DataFrame.
    """
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    return pd.read_csv(obj["Body"])

def update_datasets(initial_data, update_files, bucket_name):
    """
    Combines the initial dataset with weekly update datasets.
    If an employee already exists (by EmployeeNumber), their record is updated.
    Otherwise, the new employee record is appended.
    """
    data = initial_data.copy()
    for file_key in update_files.split(","):
        print(f"Fetching {file_key} from S3...")
        update_data = fetch_dataset(bucket_name, file_key)
        print(f"Processing update file: {file_key}")
        for _, row in update_data.iterrows():
            # Use the EmployeeNumber column as the unique identifier
            if row["EmployeeNumber"] in data["EmployeeNumber"].values:
                data.loc[data["EmployeeNumber"] == row["EmployeeNumber"], :] = row.values
            else:
                data = pd.concat([data, pd.DataFrame([row])], ignore_index=True)
    return data

def preprocess_data(data):
    """
    Prepares the dataset for training:
      - Drops or converts non-numeric and constant columns.
      - Separates the target from the features.
      - Encodes categorical variables using one-hot encoding.
    
    Returns:
      features: DataFrame of model features.
      target: Series of binary target values.
      employee_ids: Series of EmployeeNumber values for later reference.
    """
    features = data.copy()

    # Drop constant or non-informative columns
    if "Over18" in features.columns:
        features = features.drop(columns=["Over18"])
    
    # Extract and convert target (Attrition) to binary:
    # Strip whitespace and convert to lower case for robustness
    target = features.pop("Attrition").apply(lambda x: 1 if str(x).strip().lower() == "yes" else 0)
    
    # Save identifier for predictions, then drop it from training features.
    if "EmployeeNumber" in features.columns:
        employee_ids = features["EmployeeNumber"]
        features = features.drop(columns=["EmployeeNumber"])
    else:
        employee_ids = None

    # Define expected categorical columns
    expected_categorical = [
        "BusinessTravel", "Department", "EducationField", "Gender", "JobRole", "MaritalStatus", "OverTime"
    ]
    
    # Check and warn for any missing expected categorical columns
    existing_cat_cols = []
    for col in expected_categorical:
        if col in features.columns:
            existing_cat_cols.append(col)
        else:
            print(f"Warning: Expected categorical column '{col}' not found in data.")
    
    # Use one-hot encoding only on columns that exist
    if existing_cat_cols:
        features = pd.get_dummies(features, columns=existing_cat_cols, drop_first=True)
    
    # Optionally, ensure all remaining columns are numeric
    # If any non-numeric columns are found, they can be converted or dropped as needed.
    for col in features.columns:
        if features[col].dtype == "object":
            try:
                features[col] = pd.to_numeric(features[col])
            except Exception:
                print(f"Warning: Column '{col}' could not be converted to numeric and will be dropped.")
                features = features.drop(columns=[col])
    
    return features, target, employee_ids

def train_model(features, target):
    """
    Trains a decision tree classifier and prints a classification report.
    """
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return model

def predict_risk_levels(model, features, employee_ids=None):
    """
    Predicts attrition probabilities and assigns risk levels.
    Returns a DataFrame with EmployeeNumber and the corresponding AttritionRisk.
    """
    # Get probability of attrition (the second column is the probability for class '1')
    predictions = model.predict_proba(features)[:, 1]
    
    # Create risk levels using pd.cut with bins and labels.
    risk_levels = pd.cut(
        predictions,
        bins=[0, 0.33, 0.66, 1],
        labels=["Low", "Medium", "High"],
        include_lowest=True
    )
    
    # Prepare the predictions DataFrame
    if employee_ids is not None:
        predictions_df = pd.DataFrame({
            "EmployeeNumber": employee_ids,
            "AttritionRisk": risk_levels
        })
    else:
        predictions_df = pd.DataFrame({
            "AttritionRisk": risk_levels
        })
    
    return predictions_df

def save_predictions_to_s3(bucket_name, key, predictions):
    """
    Saves the predictions DataFrame as a CSV file to an S3 bucket.
    """
    local_path = "/tmp/attrition_predictions.csv"
    predictions.to_csv(local_path, index=False)
    s3 = boto3.client("s3")
    s3.upload_file(local_path, bucket_name, key)
    print(f"Predictions saved to s3://{bucket_name}/{key}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train or retrain an ML model")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["initial", "weekly"],
        default="initial",
        help="Set the training mode: 'initial' for first-time training, 'weekly' for retraining"
    )
    args = parser.parse_args()

    try:
        # Fetch initial dataset from S3
        print("Fetching initial dataset...")
        initial_data = fetch_dataset(S3_BUCKET_NAME, INITIAL_DATASET_KEY)
    
        # Combine with weekly updates if in weekly retraining mode
        if args.mode == "weekly":
            print("Running weekly retraining...")
            combined_data = update_datasets(initial_data, WEEKLY_BATCH_KEYS, S3_BUCKET_NAME)
        else:
            print("Running initial training...")
            combined_data = initial_data
    
        # Preprocess data: feature engineering, target extraction, and handling IDs
        print("Preprocessing data...")
        features, target, employee_ids = preprocess_data(combined_data)
    
        # Check for missing values and fill them (you might choose a different imputation strategy)
        if features.isnull().any().any():
            print("Warning: Missing values found in features. Filling missing values with 0.")
            features = features.fillna(0)
    
        # Train the model
        print("Training model...")
        trained_model = train_model(features, target)
    
        # Generate predictions and risk levels
        print("Predicting risk levels...")
        predictions = predict_risk_levels(trained_model, features, employee_ids)
    
        # Save the predictions back to S3
        print("Saving predictions to S3...")
        save_predictions_to_s3(S3_BUCKET_NAME, OUTPUT_PREDICTIONS_KEY, predictions)
    
        print("Workflow complete.")
    
    except Exception as e:
        print(f"An error occurred: {e}")