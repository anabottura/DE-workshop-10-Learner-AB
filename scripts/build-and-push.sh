#!/bin/bash

# Variables
ECR_REPO_URI="<your-ecr-repo-uri>"
IMAGE_NAME="hr-ml-model"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Tag the image
docker tag $IMAGE_NAME:latest $ECR_REPO_URI:latest

# Authenticate with ECR
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin $ECR_REPO_URI

# Push the image
docker push $ECR_REPO_URI:latest
