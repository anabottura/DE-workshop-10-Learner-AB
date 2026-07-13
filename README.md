**“What’s the cost of a 30-minute pipeline failure?”**

AWS estimates that a 30-minute outage at a major financial services company can cost £3 million in lost transactions.
Google Cloud’s SLA guarantees 99.95% uptime—but do you know how they achieve that? **Orchestration**.
Your data pipeline could cost your company thousands per minute if it goes down—so let’s make sure that never happens.

# Data Engineer Workshop 10: Conducting Your Data Orchestration

Materials:

**Slides** on advanced container orchestration (Argo and related concepts).
**Docker** code in the `docker/` folder, including `Dockerfile` and `train_model.py`.
**Argo** YAML in `argo/`, demonstrating how to run ephemeral ML steps.
**Kubernetes** manifests in `kubernetes/` for potential microservices or service definitions.
**Scripts** (optional) to automate certain tasks like building images or tearing down the environment.
**Data** The initial data file (0) is sourced from Kaggle (the IBM HR Attrition dataset). The incremental batches (1) and (2)  bring your HR ML pipeline closer to real-world conditions (changed data, new hires. 

We will be orchestrating retraining steps through ephemeral container workflows. It’s a perfect example of how a microservices + orchestration environment (Argo on EKS) simplifies repeated tasks and ensures your HR analytics pipeline stays up-to-date with minimal fuss.

All the tasks are documented as separate chapters in your repository. Suggested timings look as follows:

### **🕘 Duration**

-   **Morning Session**: 10:00 -- 13:00
-   **Lunch Break**: 13:00 -- 14:00
-   **Afternoon Session**: 14:00 -- 16:00

* * * * *

### **🎯 Workshop Objectives**

By the end of this workshop, learners will:

1.  Understand the importance of **orchestration in data engineering**.
2.  Implement **MLOps practices** for automating ML workflows.
3.  Use **AWS CloudFormation** to deploy infrastructure as code.
4.  **Containerise ML models** using Docker and manage them in Amazon ECR.
5.  **Orchestrate ML workflows** with Argo Workflows on Amazon EKS.
6.  Apply orchestration techniques to **predict employee attrition risks** using ML.

* * * * *

### **📜 Tentative schedule (this will vary on the day)**

| **Time** | **Session** | **Key Activities** |
| --- | --- | --- |
| **09:30 -- 10:15** | Introduction, slides | Overview of orchestration, workshop objectives |
| **10:30 -- 11:00** | Infrastructure as Code (IaC) | Deploying AWS resources (Tasks 0 and 1) |
| **11:15 -- 12:00** | Begin Task 2 | Build + push container, configure K8S, install Argo |
| **11:30 -- 12:30** | Use this task for troubleshooting and updating a learning journal |
| **12:30 -- 13:30** | **Lunch Break** | - |
| **13:30 -- 14:15** | Finish Task 2 | Submit workflows, examine logs and outputs |
| **14:15 -- 15:00** | Variable Part | Troubleshoot or Extension (1): Examining non-Argo Kubernetes jobs |
| **15:00 -- 15:30** | Wrap-up Part | Troubleshoot or Extension (2): Examining GitHub actions |
| **15:30 -- 16:00** | Validation & Summary | Understanding predictions, debugging, improving efficiency |
| **16:00 -- 16:30** | Group discussion, slides |

* * * * *

### **🛠 Workshop Hands-On Tasks**

Today's tasks have been documented thoroughly for you, with step-by-step guidance, so you're in safe hands.
You can access the MD files with the tasks, directly from the root directory of the repo.
However, the preferred way is to access the jupyter book that combines all the tasks with a search function.
To do that, navigate to the top of this document and click on the jupyter book URL provided.

List of tasks.

-   **[Task 0](https://github.com/anabottura/DE-workshop-10-Learner-AB/blob/main/Task_0_INTRO.md)** (Intro): Read the **Introduction to Orchestration & MLOps** 
-   **[Task 1](https://github.com/anabottura/DE-workshop-10-Learner-AB/blob/main/Task_1.md)**: Deploy AWS resources using **CloudFormation & IAM** 
-   **[Task 2](https://github.com/anabottura/DE-workshop-10-Learner-AB/blob/main/Task_2.md)**: Containerise ML models & orchestrate workflows with **EKS & Argo**
-   **[Task 3](https://github.com/anabottura/DE-workshop-10-Learner-AB/blob/main/Task_3_Wrapping_Up.md)**: Examine additional elements of your GitHub Repo

* * * * *

### **📌 Key Learning Points (Preview)**

-   **Scalability**: Automating infrastructure deployment with IaC.
-   **Portability**: Managing ML workflows in containers with Docker & Kubernetes.
-   **Automation**: Orchestrating workflows with Argo & CI/CD.
-   **Monitoring & Debugging**: Retrieving logs, tracking model predictions.