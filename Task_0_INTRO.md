# Level 5 Data Engineer Workshop 10: Conducting Your Data Orchestration

## Task 0: Read the Following Introduction and Motivation for this Month's Topic

### 🔙 Reminder of Workshop 9 — Advanced Stream Processing 🔙

In your previous **Workshop 9**, we introduced advanced streaming pipelines, focusing on how data could be ingested in near real time for downstream analytics. We explored the benefits of real-time ingestion, best practices for setting up data streams, and the fundamentals of building a "continuously updating" data platform. 

We will be building on this prior knowledge of **ingestion** in our current workshop to simulate updates to Machine Learning datasets in a real-world HR environment.

### Question for learners 🙋 

Can you think of a scenario where streaming alone isn’t enough, and a more generalised orchestration layer becomes essential?

_Hint: Consider situations where different data sources need to be synchronised._

### Orchestration with EKS and Argo — What’s Different Now ⁉️

In this new workshop (Workshop 10), we shift from stream processing to end-to-end orchestration for a machine learning (ML) workflow. Rather than focusing on continuous data ingestion, we’ll emphasise how to automate and manage container-based tasks in AWS for the HR Attrition(*) use case that your PDE will have helped you explore (see: session slides). 

_(*) HR Attrition simply means staff turnover_

Think about stages like data cleansing, feature engineering, model training, and model evaluation, all running as containers with dependencies on each other. These stages are required because: (a) HR data normally comes from disparate sources, and a considerable amount of "data wrangling" is needed to make it usable; and (b) machine learning often requires some trial and error to get right when building a new model.

Our scenario involves the weekly retraining of a decision-tree model, which needs to fetch new data, run transformations, train, validate, and deploy the model. Streaming only handles the data arrival, but not the multi-step, container-based tasks with dependencies.

## But what the heck are containers, really?

Containers are technologies that allow the packaging and isolation of applications with their entire runtime environment. Essentially, you can think of them as being like lightweight virtual machines. They are useful to make different applications and services independent of each other. These independent apps/services are often called microservices, because they're so lightweight and "microscopic". So in your HR case study, you could have a system that relies on two containerised microservices - for example - an ingestion microservice running its own container, and also a notification-sending microservice running in its separate very own container.

🔙You may remember that when you completed the introductory SQL exercises in unit _“2.1 Core SQL and Python for Data Engineering”_, we introduced you to ECR - Amazon's elastic container registry. In that module, you used PgAdmin, which ran in a so-called "Docker container", and ECR was used to register, manage and deploy the container image.🔙

## But what the heck is orchestration, really?

Orchestration is fast becoming the bread and butter of Data Engineering so let's try and explain what it is! Imagine you have a detailed flowchart showing how different business tasks should work together (for example, sales, dispatch, and invoicing). That flowchart is like a blueprint; it illustrates what ought to happen and in what order, but it does not automatically set the processes in motion. You need someone (or something) to read that blueprint, trigger each task at the proper moment, and ensure everything is executed correctly, even if one task falters. In data engineering, that someone is known as an **orchestrator**, and normally it's a program, not a human person.

Below are a few ways to understand orchestration:

### 1. The Business Blueprint Analogy

- **Blueprint versus Execution:**  
  Think of a business process diagram drawn on paper or in software. It maps out how processes like order fulfilment should occur. However, simply drawing the diagram will not set orders rolling or ensure invoices are dispatched.  
- **Orchestration Role:**  
  Orchestration is like appointing a dedicated operations manager who interprets the diagram and then triggers tasks at the correct times, manages dependencies (ensuring dispatch happens after order confirmation), and retries tasks if something goes awry (for instance, reprocessing a failed invoice). In data engineering, an orchestration framework does that, and it uses containers to isolate different types of tasks.

### 2. The Kitchen Conductor Analogy
- **Kitchen Workflow:**  
  Imagine a bustling restaurant kitchen in a cosy market town. Several chefs are working on different parts of a meal (starters, main courses, puddings).  
- **Orchestration Role:**  
  The head chef (or kitchen manager) coordinates the timing, ensuring that the starter is ready to be served before the main course arrives, manages dependencies by making sure that the sauce is prepared before it is needed on the dish, and addresses any mishaps swiftly (say, if a dish does not come out quite right) so that service remains smooth.  
  Similarly, an orchestrator in data engineering coordinates various jobs (data extraction, transformation, loading) so that the overall process runs seamlessly. This is an example of orchestration using *workflows*.

### 3. The Train System Analogy
- **Train Scheduling:**  
  Consider Network Rail, where trains need to arrive, depart, and switch tracks at precisely the right moments. A central scheduling system is indispensable to avoid delays and mishaps.  
- **Orchestration Role:**  
  In data workflows, the orchestrator functions like the railway scheduling centre by scheduling tasks (ensuring each train is on time), managing dependencies (making certain that one train waits until the previous one has safely departed), and handling errors (rerouting or retrying tasks if a train or process is delayed). All these tasks are containerised.

## Key Elements of Orchestration in Data Engineering

From the examples above, we can identify the key elements of an effective orchestration framework:

- **Scheduling and Automation:**  
  The orchestrator automatically initiates containerised tasks based on a predetermined timetable or specific events (such as the arrival of a new data file).

- **Dependency Management:**  
  It ensures containerised tasks are executed in the proper sequence; for example, data must be extracted before it can be transformed and loaded.

- **Error Handling and Recovery:**  
  If a containerised task fails, the orchestrator can automatically attempt a retry, alert an engineer, or execute a contingency process.

- **Resource Management:**  
  In a cluster or cloud environment, orchestration helps distribute containers with tasks across available resources, ensuring optimal performance without a hitch.

- **Monitoring and Logging:**  
  It keeps an eye on the progress of each task, logs outcomes, and provides dashboards to monitor the health of the workflow, making it easier to pinpoint and rectify issues.

- **Scalability and Resilience:**  
  An orchestrator supports scaling (running containers in parallel when possible) and builds resilient data pipelines.


## Applying Orchestration in Practice

We now see how **Orchestration** in data engineering is akin to the invisible conductor behind a well-rehearsed performance. Whether you are picturing a business process that requires a manager to execute its steps, a head chef in a bustling kitchen, or a railway scheduling centre keeping trains on time, orchestration ensures that each component of a complex data pipeline runs at the right moment, in the correct sequence, and recovers gracefully from any setbacks. It transforms static workflows (merely drawn diagrams) into dynamic, automated processes that keep your data flowing reliably.

Let’s reflect on how Workshop 10’s orchestration approach might fit alongside the data pipeline patterns you've learned from your previous workshops:

1. **Workshop 9: Advanced Stream Processing**  
   - **What we did**: Built real-time ingestion for continuous data flows.  
   - **Practical learning**: Real-time data is powerful but may only address the *input* side; you still need to coordinate tasks like transformations, model retraining, or notifications.

2. **Workshop 10: Orchestration of ML Workflows (Today)**  
   - **What we’ll cover**: Deploying containers to a Kubernetes cluster (EKS), scheduling multi-step jobs with Argo, managing ML tasks end-to-end.  
   - **Project question**: If your data arrives in bursts (batch) or you need consistent multi-stage ML processes, how will you ensure tasks run reliably, in the correct sequence, with minimal manual intervention?


By layering orchestration on top of streaming or batch ingestion, you gain an entire **MLOps** approach that ensures your data-driven processes run consistently, reliably, and transparently. MLOps, or Machine Learning Operations, is a set of practices that help manage the machine learning (ML) lifecycle in data engineering.


### Moving Forward With Your Learning

Today, we’re focusing on how to spin up, orchestrate, and **monitor** a container-based ML workflow for **HR Employee Attrition** (staff turnover). In particular:

1. **Docker & ECR**: Ensure your model container is built once, run anywhere, and versioned in ECR.  
2. **Kubernetes on EKS**: Provide the core scheduling and resource management for container workloads.  
3. **Argo**: Add the orchestration logic to chain tasks (data prep, model training, risk classification) in the correct order.  

Our scenario does not currently use streaming, but assumes that you are able to run batch data extracts on a schedule, then orchestrate ML tasks each night. With batch processing, the same data quality caveats apply as with streaming, with some differences (think: timeliness).

(_Re-cap: What do we mean by data quality dimensions?_)

Remember to review the slide decks (morning and afternoon to clarify certain areas that may still be confusing. Ask your PDE if you have any questions.)

---

## Alignment with Data Engineer Pass Descriptors 📖📖📖

This workshop aligns with several IFATE Data Engineer Pass Descriptors:  
- **(K8)** Explains the deployment approaches for new data pipelines and automated processes.  
- **(K6)** Describes software development principles and DevOps practices, such as version control and CI/CD, relevant to data engineering.  
- **(K20)** Demonstrates knowledge of data engineering tools and how they are applied for container-based workflows.  
- **(S15)** Integrates tasks for on-demand, streaming, or scheduled data ingestion steps.  
- **(B1, B2)** Exhibits proactive collaboration and accountability, crucial when orchestrating multi-team pipelines in production.

- **(K8)**: By automating deployments of EKS clusters, containers, and orchestrators, we demonstrate best practices for delivering robust data pipelines quickly and consistently.  
- **(K6)**: Emphasises DevOps-like approaches to data engineering—utilising version control, container registries, and CI/CD for rapid iteration.  
- **(K20)**: Container-based ML flows and the orchestration of tasks are among the “data engineering tools” that learners apply to their own organisations.  
- **(S15)**: “Optimises data ingestion processes” can also include orchestrated tasks that prepare data, schedule model training, or manage job dependencies in real time or on demand.  
- **(B1, B2)**: Demonstrating collaborative ways of working—coordinating data scientists, ML engineers, and platform teams—to ensure an orchestrated pipeline meets business requirements.


## Ready for Today’s Workshop Scenario and Objectives? ✔️✅☑️

So, do you feel ready for today's workshop? In short, you’ll implement an orchestrated ML pipeline that retrains an HR Attrition (staff turnover) model regularly and publishes risk classifications to an S3 location. By the end, you will have:

- **Built** a minimal EKS cluster and an ECR repository.  
- **Packaged** the HR model and training code as a container.  
- **Scheduled** or **triggered** ML tasks with Argo.
- **Demonstrated** how to monitor container logs and pipeline success.  
- **Reflected** on how orchestration ensures repeatability, resilience, and traceability.

This workshop gives you **hands-on** experience tying everything together: from Docker build → ECR push → Kubernetes deployments → orchestrating multi-step workflows → verifying logs and outcomes. You’ll see how each workshop concept (data ingestion, containerisation, cloud deployment) folds into a cohesive, production-like scenario.

We focus on the *orchestration* aspect, not model accuracy. The ML steps are purposefully simplified to highlight how you’d schedule, manage, and monitor container-based tasks rather than produce a best-in-class HR model.

Ready? Feel free to get started on Task 1!