# Data Engineer Workshop 10: Conducting Your Data Orchestration

## ⚙️ Task 3: Re-cap and optional stretch/extend with GitHub Actions

## Workshop Objectives Recap ✔️

By the end of this task, you have:

- Deployed a minimal cloud infrastructure with CloudFormation.
- Configured a containerized ML pipeline in ECR and EKS.
- Verified the orchestration setup with Argo Workflows.
- Ran the HR ML pipeline and verified the predictions it generated.

## 🏁 Wrapping Up and Additional Resources

In this workshop, you’ve learned how Data Engineers turn away from lots of ad-hoc scripts or one-off schedules towards a **robust orchestrator** that coordinates each stage of their pipelines, such as in the case of your HR Attrition ML workflow. You used a **container image** pushed to ECR, spun up ephemeral tasks on an EKS cluster that used that container image, and leveraged **Argo** to define dependencies, monitor runs, and handle any errors in the HR Workflow. The successful workflow run has generated useful predictions that can be used by HR to inform their strategy.

1. **Why Orchestration?**  
   - Consistent, repeatable ML processes  
   - Clear scheduling & dependency management  
   - Easier troubleshooting & auditing  

2. **Integrating with Your Existing Projects**  
   - Combine orchestrated tasks with streaming or batch ingestion from prior workshops  
   - Incorporate more advanced tasks: data validation, multi-environment deployments, etc.  
   - Gradually refine security, networking, secrets management for a production-level solution  

3. **Looking Ahead / Stretch Challenge 🏋️‍♂️**  
   - For your stretch/extend deliverables, consider how you’ll embed these orchestrations into a broader data platform.Consider how you might extend this pipeline:
    - Adding steps for data validation or notifications.
    - Enabling dynamic scaling of tasks based on resource usage.
    - Experiment with more complex workflows involving branching and conditional logic.

Next steps might include even more advanced integrations/notifications, more robust partial re-trains on new data, or multi-model deployments.

Take time to reflect on how orchestration can unify the pipeline building, container usage, scheduling, and best practices in data engineering. The skills you used—like Docker, EKS, CI/CD—build upon everything from the earlier workshops in a cohesive manner.

Additional Resources
- **AWS EKS Documentation**: [https://docs.aws.amazon.com/eks/](https://docs.aws.amazon.com/eks/)  
- **Apache Airflow on Kubernetes**: [https://airflow.apache.org/docs/kubernetes.html](https://airflow.apache.org/docs/kubernetes.html)  
- **Argo Workflows**: [https://argoproj.github.io/argo-workflows/](https://argoproj.github.io/argo-workflows/)  
- **Docker Official Docs**: [https://docs.docker.com/](https://docs.docker.com/)  

In a production environment, you’d typically add further layers: custom networking, locked-down IAM roles, integrated secrets, robust logging, and so on. This workshop focuses on the essential orchestrated ML pipeline with enough structure to be realistic yet remain teachable in a single session.

## Stretch your automation with GitHub Actions

GitHub Actions will be explored in your future e-learning very soon.

If you found yourself having some extra time at the end of this workshop, keep reading (as a stretch/extend activity - it's optional.)

GitHub Actions are not really "orchestration", they belong to the "CI/CD" category (continuous integration/continuous deployment), but __both orchestration and CI/CD can be thought of as *automation*__. As a Data Engineer, you should familiarise yourself with different approaches to automation. Automation is what makes processes repeatable and manageable and maps directly to many of your KSBs.

The Github Actions are included in your GitHub repo and free for you to experiment with as a stretch/extend activity for motivated learners. Most of them will only execute on the staging branch (ignored on main branch). Ensure that you replace <YOUR_ACCOUNT_ID> and <YOUR_ACCOUNT_ID> in the AWS credential steps to make your experiments successful.

GitHub Actions is a continuous integration and continuous deployment (CI/CD) platform that allows you to automate your build, test, and deployment processes directly from your GitHub repository. In this workshop, we have included some GitHub Actions workflows as an optional stretch/extend activity for those who are keen to experiment further with automation. These workflows automatically run on the staging branch and are intentionally configured to be ignored on the main branch. This ensures that your primary codebase remains unaffected while you explore automation features.

**The GitHub Actions workflows in this repository help automate tasks such as:**

   -  Linting and validating the CloudFormation templates.
   -  Running basic Python linting checks on the Docker scripts.
   -  Building and pushing the Docker image to Amazon ECR (Elastic Container Registry).
   -  Optionally deploying the CloudFormation stack to AWS.

By experimenting with these actions, you will gain practical insights into how CI/CD pipelines work, and how automated processes can improve the reliability and speed of your development and deployment cycles.

Reflect on how orchestration could be integrated with CI/CD automation in your enterprise, to make your own data pipelines more robust.

**Configuration Requirements:**

Remember that to successfully run these workflows, you must replace the placeholder <YOUR_ACCOUNT_ID> in the AWS credential steps with your actual AWS account ID. This change is necessary to ensure that the actions can authenticate with AWS and perform tasks such as logging into ECR and deploying CloudFormation stacks.

*Why Explore GitHub Actions?*

In a professional environment, automating build and deployment tasks is crucial. GitHub Actions is one of the many tools that can help streamline these processes, reducing manual errors and saving time Experimenting with GitHub Actions during this workshop will provide you with a real-world understanding of how CI/CD pipelines are set up and managed, which is a valuable skill in data engineering and DevOps (as well as MLOps) practices. Remember, examining GitHub Actions workflows is entirely optional, so if you’re not yet comfortable with CI/CD or GitHub Actions, you can focus on the primary workshop tasks and come back to these activities later.

## Extra notes: When to Use the provided build-and-push.sh and tear-down.sh scripts ##

The build-and-push script is provided as a convenience for learners who wish to manually build the Docker image for the ML model and push it to your Amazon ECR repository. You might use this script if you prefer to work from the command line or if you want to verify the build process independently of the GitHub Actions workflows. Before running the script, ensure you have replaced the placeholder <your-ecr-repo-uri> with your actual ECR repository URI and <your-region> with your AWS region. 

The build-and-push script performs the following steps:

   -  Builds the Docker image using the Dockerfile in the repository.
   -  Tags the image with the appropriate ECR URI.
   -  Authenticates with ECR.
   -  Pushes the image to ECR so that it can be used by your Kubernetes deployments and Argo Workflows.


The tear-down script is intended to help you clean up your AWS environment after the workshop. Once you have finished experimenting with the orchestration pipeline, you can use this script to delete the CloudFormation stack that was used to provision your AWS resources. This is particularly useful if you want to avoid incurring unnecessary costs or if you wish to start from scratch in a later session. Before running the script, ensure that the STACK_NAME variable is set to the name of the stack you wish to delete (for example, ws10-orch-stack).

## Optional Extension - Examining the non-Argo Kubernetes YAML files in the repo


**1\. What are those Kubernetes YAML Files Doing in "kubernetes/" in GitHub?**
-------------------------------------------------

There are some extra Kubernetes files given to you to have a look at as a stretch/extend activity.

-   **S3 Driver, Persistent Volume and Persistent Volume Claim (in the _experimental_ folder)**\
    Defines persistent storage simulated on top of S3 that allows data to be retained between pods.
-   **ConfigMaps (`configmap.yaml`, if any exists)**\
    Provides environment configurations for Kubernetes workloads.
-   **Service files**\
    Defines microservices that could run persistently in Kubernetes: ingestion and notification jobs.
-   **Train job**\
    Exposes the ML training job container to external or internal consumers.


* * * * *

**2\. Do These Files Replace My Argo Workflow?**
------------------------------------------------

**No**, they do **not** replace the Argo workflow but instead serve a **different purpose**:

-   **Argo Workflows** → Manages ML training as **one-off, ephemeral workloads** that get triggered manually or on a schedule.
-   **Kubernetes Deployments & Services** → Keep a **long-running** container available in EKS.

If you want to run your ML pipeline as **a job that executes and terminates**, use **Argo Workflows**.\
If you need a **service that stays up** and allows users to query the trained model, **use Kubernetes Deployments & Services** (this would be an extend/stretch activity as there is simply not enough time for you to experiment with this setup in the workshop.)
Note: In train-job.yaml, ensure that the placeholder <ECR_REPO_URI> is replaced by the actual URI from your CloudFormation outputs.

**Optional: a more in-depth explanation of the extra YAML files**
If you have some spare time after the workshop, you could experiment with several Kubernetes YAML files that help manage and orchestrate different components of our ML pipeline on the EKS cluster. These files work together to configure, deploy, and run extra services that you could develop - ranging from data ingestion to model training.

### Closer look at `configmap.yaml`

This file creates a Kubernetes **ConfigMap** named `train-model-config`. It stores essential configuration data (such as the S3 bucket name) that the ML training job needs. By referencing this ConfigMap, the training job can set environment variables dynamically, ensuring the container accesses the correct S3 bucket for its data. Make sure you update the values inside this file. (Note that if you're using Argo, this config map is __ignored__).

### `ingestion_service.yaml`

The `ingestion_service.yaml` file defines a Kubernetes **Deployment** for a simple data ingestion service. It is not a fully fledged service and serves as a POC (proof-of-concept). This POC service uses the AWS CLI image to copy data from an S3 bucket to a local directory within the pod. Although not part of the core ML pipeline, this deployment demonstrates how Kubernetes can automate data ingestion tasks and is useful for preparing data before processing.

### `notification-service.yaml`

This POC YAML file deploys a simulated **notification service**. In a real-world scenario, such a service might send alerts or trigger other processes when a job completes or if an error occurs. Here, it simply prints a message to confirm that a notification has been triggered, illustrating how notifications can be integrated into your orchestration workflow. This serves as inspiration for motivated learners to build something on top of this skeleton (think about ideas for your Endpoint Assessment Project!)

### `persistent_volume_claim.yaml`

The `persistent_volume_claim.yaml` file defines a **PersistentVolumeClaim (PVC)** named `ml-pipeline-volume`. This PVC could be used by the ML training job to provide persistent storage (e.g. storage that won't disappear after the job finishes running). Such storage is critical for holding  intermediate outputs generated between the training process and the re-training processes, ensuring data is retained even if the pod restarts. In Argo, we decided to ignore this file, as our ML model accesses S3 directly from its Python code.

### `train-job.yaml`

This file defines a Kubernetes **Job** that runs the ML training model as a one-off task.  Remember that this job is different from your Argo workflow, even if there are similarities. Key points include:

-   The non-Argo job still references the same Docker image that you have built and pushed to your ECR repository.
-   It sets environment variables (such as the S3 bucket name and output key) by referencing the `train-model-config` ConfigMap.
-   The Job is designed to execute once, triggering the ML training process within the cluster.

Each of these Kubernetes YAML files plays a specific role in orchestrating the overall workflow. Together, they demonstrate how to leverage Kubernetes for managing containerised applications in a production-like environment, without argo. Only focus on examining those optional files if you are confident with all the work you've done so far and need a challenge to stretch yourself. Remember they're experimental and your PDE may be unable to fully assist. In the workshop, we do not use this job, we use the Argo equivalent.

## Thank you!

Thank you for completing Workshop 10! Good luck with the rest of your Data Engineer journey!

Remember: always think about how to re-use the KSBs you learn in these workshops, both for your job/work role, and for your EPA (endpoint assessment)!