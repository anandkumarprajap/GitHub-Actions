# GitHub Action Practics 

## Concepts

# 1. Workflows

To Create a GitHub Actions workflow you need a folder called .github/workflows

.............................Practice steps...................................
![Image 1](1.png)
![Image 2](2.png)
![Image 3](3.png)
![Image 4](4.png)
![Image 5](5.png)
![Image 6](6.png)
![Image 7](7.png)
![Image 8](8.png)
![Image 9](9.png)
![Image 10](10.png)
![Image 11](11.png)
![Image 12](12.png)
![Image 13](13.png)
![Image 14](14.png)
![Image 15](15.png)
![Image 16](16.png)
![Image 17](17.png)
![Image 18](18.png)
![Image 19](19.png)
![Image 20](20.png)
![Image 21](21.png)
![Image 22](22.png)
![Image 23](23.png)
![Image 24](24.png)



# GitHub Actions & CI/CD — Beginner Notes

## 1. What is CI/CD?

**CI/CD = Continuous Integration / Continuous Delivery (or Deployment)**

CI/CD is a software development practice that automates:

```text
Build → Test → Package → Deploy
```

### Simple CI/CD Flow

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----> Build
    |
    +----> Test
    |
    +----> Docker Build
    |
    +----> Deploy
    |
    v
Server / Cloud
    |
    v
End User
```

---

# 2. What is GitHub Actions?

**GitHub Actions** is GitHub's automation and CI/CD platform.

It allows us to automatically execute tasks when an event occurs in a GitHub repository.

Example:

```text
git push
   |
   v
GitHub Actions
   |
   +----> Install dependencies
   |
   +----> Build application
   |
   +----> Run tests
   |
   +----> Build Docker image
   |
   +----> Deploy application
```

Instead of manually performing these tasks every time, GitHub Actions automates them.

---

# 3. When was GitHub Actions Introduced?

GitHub Actions was announced at **GitHub Universe in October 2018** as a developer preview.

It became **generally available on November 13, 2019**.

```text
GitHub Actions
      |
      +---- Announced: October 2018
      |
      +---- Generally Available: November 13, 2019
```

---

# 4. Why Use GitHub Actions?

Without CI/CD:

```text
Developer
   |
   v
Manually Build
   |
   v
Manually Test
   |
   v
Manually Create Docker Image
   |
   v
Manually Deploy
   |
   v
Server
```

With GitHub Actions:

```text
Developer
   |
   | git push
   v
GitHub
   |
   v
GitHub Actions
   |
   +---- Build
   +---- Test
   +---- Docker Build
   +---- Deploy
   |
   v
Server
```

### Main Benefits

* Automation
* Faster development
* Automated testing
* Consistent deployments
* Less manual work
* Repeatable processes
* Integration with GitHub
* Docker integration
* Kubernetes integration
* Cloud deployment integration

---

# 5. CI — Continuous Integration

CI mainly focuses on integrating and validating code changes.

Typical CI activities:

```text
Code
  |
  v
Build
  |
  v
Test
  |
  v
Code Quality
  |
  v
Security Scan
```

Example:

```text
Developer
    |
    | git push
    v
GitHub
    |
    v
GitHub Actions
    |
    +---- Build
    |
    +---- Unit Test
    |
    +---- Lint
    |
    +---- Security Scan
```

---

# 6. CD — Continuous Delivery / Deployment

CD takes validated application code toward release and deployment.

```text
Build
  |
  v
Test
  |
  v
Docker Image
  |
  v
Container Registry
  |
  v
Deploy
  |
  v
Server / Kubernetes
```

## Continuous Delivery

The application is automatically prepared for release.

Production deployment may require approval.

```text
Code
  |
  v
Build
  |
  v
Test
  |
  v
Package
  |
  v
Ready for Production
  |
  v
Manual Approval
  |
  v
Production
```

## Continuous Deployment

Deployment happens automatically after successful checks.

```text
Code
  |
  v
Build
  |
  v
Test
  |
  v
Package
  |
  v
Automatic Deploy
  |
  v
Production
```

---

# 7. Complete CI/CD Pipeline

```text
                    CI
          <------------------->

Developer
    |
    | git push
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +-------------------------+
    |                         |
    v                         v
Checkout Code          Install Dependencies
    |                         |
    +------------+------------+
                 |
                 v
               Build
                 |
                 v
                Test
                 |
                 v
        Code Quality /
        Security Scan
                 |
                 v
           Docker Build
                 |
                 v
          Docker Image
                 |
                 v
        Docker Registry
                 |
                 v
                    CD
          <------------------->

              Deploy
                 |
                 v
        Server / Kubernetes
                 |
                 v
            Application
                 |
                 v
             End User
```

---

# 8. CI/CD Tools Available in the Market

GitHub Actions is one CI/CD tool.

Other commonly used tools include:

| Tool                   | Main Use             |
| ---------------------- | -------------------- |
| GitHub Actions         | CI/CD                |
| GitLab CI/CD           | CI/CD                |
| Jenkins                | CI/CD Automation     |
| CircleCI               | CI/CD                |
| Bamboo                 | CI/CD                |
| TeamCity               | CI/CD                |
| Azure DevOps Pipelines | CI/CD                |
| AWS CodePipeline       | AWS CI/CD            |
| Argo CD                | Kubernetes GitOps CD |
| Flux CD                | Kubernetes GitOps CD |

---

# 9. GitHub Actions vs GitLab CI/CD

Both can automate CI/CD.

### GitHub

```text
GitHub
   |
   v
GitHub Actions
```

Workflow files:

```text
.github/workflows/*.yml
```

### GitLab

```text
GitLab
   |
   v
GitLab CI/CD
```

Common configuration file:

```text
.gitlab-ci.yml
```

---

# 10. CI Tools and CD Tools

Some platforms provide both CI and CD capabilities:

```text
GitHub Actions
GitLab CI/CD
Jenkins
Azure DevOps
CircleCI
```

Some tools are particularly focused on Kubernetes CD / GitOps:

```text
Argo CD
Flux CD
```

Example:

```text
GitHub Actions
       |
       | Build + Test
       v
Docker Image
       |
       v
Container Registry
       |
       v
Argo CD
       |
       v
Kubernetes
```

---

# 11. GitHub Actions — Important Concepts

The basic hierarchy is:

```text
Workflow
   |
   +---- Job
           |
           +---- Step
                   |
                   +---- Command
                   |
                   +---- Action
```

Remember:

```text
Workflow
    ↓
Jobs
    ↓
Steps
    ↓
Commands / Actions
```

---

# 12. Workflow

A **workflow** is an automated process defined in a YAML file.

GitHub Actions workflow files are normally stored here:

```text
.github/workflows/
```

Example:

```text
.github/
└── workflows/
    └── hello.yml
```

A workflow tells GitHub:

> When this event happens, execute these jobs and steps.

---

# 13. Job

A **job** is a group of steps that execute together on a runner.

Example:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

Structure:

```text
Workflow
    |
    └── build Job
```

---

# 14. Step

A **step** is an individual task inside a job.

Example:

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4

  - name: Run test
    run: npm test
```

A step can use:

```yaml
uses:
```

or execute:

```yaml
run:
```

---

# 15. Action

An **Action** is a reusable, pre-built automation component.

Example:

```yaml
uses: actions/checkout@v4
```

`actions/checkout` is a pre-built GitHub Action.

It checks out the repository code so that later steps can work with it.

Think:

```text
Action = Reusable pre-built automation
```

Examples:

```yaml
uses: actions/checkout@v4
```

```yaml
uses: actions/setup-node@v4
```

```yaml
uses: actions/setup-python@v5
```

---

# 16. Command

A command is a command executed directly on the runner.

Example:

```yaml
run: npm install
```

Another:

```yaml
run: npm test
```

Another:

```yaml
run: docker build -t myapp .
```

Remember:

```text
uses:
    ↓
Use a pre-built Action

run:
    ↓
Execute a command
```

---

# 17. GitHub Actions YAML Structure

GitHub Actions workflows use YAML.

Example:

```yaml
name: Hello GitHub Actions

on:
  push:

jobs:
  hello:
    runs-on: ubuntu-latest

    steps:
      - name: Print message
        run: echo "Hello GitHub Actions"
```

Structure:

```text
name
 |
 v
on
 |
 v
jobs
 |
 +---- Job
        |
        +---- runs-on
        |
        +---- steps
                |
                +---- uses
                |
                +---- run
```

---

# 18. Important GitHub Actions YAML Keywords

## `name`

Defines the workflow name.

```yaml
name: CI Pipeline
```

---

## `on`

Defines when the workflow should run.

```yaml
on:
  push:
```

Example:

```yaml
on:
  push:
    branches:
      - main
```

Meaning:

```text
Push to main
     |
     v
Workflow starts
```

---

## `jobs`

Defines the jobs in the workflow.

```yaml
jobs:
```

---

## `runs-on`

Defines the runner/environment.

```yaml
runs-on: ubuntu-latest
```

---

## `steps`

Defines individual tasks.

```yaml
steps:
```

---

## `uses`

Uses a pre-built Action.

```yaml
uses: actions/checkout@v4
```

---

## `run`

Runs a shell command.

```yaml
run: npm test
```

---

# 19. GitHub Actions Basic Diagram

```text
.github/
   |
   └── workflows/
          |
          └── hello.yml
                   |
                   v
               Workflow
                   |
                   v
                  Job
                   |
                   v
                 Steps
                   |
             +-----+-----+
             |           |
           uses          run
             |           |
             v           v
           Action     Command
```

---

# 20. First GitHub Actions Practice

## Step 1 — Create a GitHub Repository

Create a new repository on GitHub.

Example repository name:

```text
github-action-practice
```

Repository:

```text
github-action-practice
```

---

# 21. Step 2 — Create Repository

Create:

```text
github-action-practice
```

Initialize it with:

```text
README.md
```

Initial structure:

```text
github-action-practice/
└── README.md
```

---

# 22. Step 3 — Create Workflow Directory

Inside the repository create:

```text
.github
```

Inside `.github` create:

```text
workflows
```

Inside `workflows` create:

```text
hello.yml
```

Final structure:

```text
github-action-practice/
│
├── README.md
│
└── .github/
    └── workflows/
        └── hello.yml
```

> **Important:** The correct directory is `.github/workflows/`.

---

# 23. Step 4 — Create `hello.yml`

File:

```text
.github/workflows/hello.yml
```

Code:

```yaml
name: Hello GitHub Actions

on:
  push:

jobs:
  hello:
    runs-on: ubuntu-latest

    steps:
      - name: Print Hello Message
        run: echo "Hello GitHub Actions"
```

---

# 24. Understand `hello.yml`

## Workflow Name

```yaml
name: Hello GitHub Actions
```

This gives the workflow a name.

```text
Workflow
    |
    └── Hello GitHub Actions
```

---

## Trigger

```yaml
on:
  push:
```

This means the workflow runs when a push occurs.

```text
git push
   |
   v
Workflow starts
```

---

## Job

```yaml
jobs:
  hello:
```

The workflow contains a job called `hello`.

```text
Workflow
   |
   └── hello Job
```

---

## Runner

```yaml
runs-on: ubuntu-latest
```

The job runs on an Ubuntu GitHub-hosted runner.

```text
Job
 |
 v
Ubuntu Runner
```

---

## Step

```yaml
steps:
  - name: Print Hello Message
```

The job contains a step.

---

## Command

```yaml
run: echo "Hello GitHub Actions"
```

This executes:

```bash
echo "Hello GitHub Actions"
```

---

# 25. Complete Execution Flow

```text
Developer
    |
    | Commit / Push
    v
GitHub Repository
    |
    v
.github/workflows/hello.yml
    |
    v
GitHub Actions
    |
    v
Workflow
    |
    v
Job: hello
    |
    v
Ubuntu Runner
    |
    v
Step
    |
    v
run: echo "Hello GitHub Actions"
    |
    v
Output:
Hello GitHub Actions
```

---

# 26. Real CI/CD Example

Suppose we have a MERN application.

```text
Developer
   |
   | git push
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +-----------------------+
   |                       |
   v                       v
Checkout Code        Install Dependencies
   |                       |
   +-----------+-----------+
               |
               v
             Test
               |
               v
             Build
               |
               v
         Docker Build
               |
               v
       Docker Image
               |
               v
      Container Registry
               |
               v
        Deploy Server
               |
               v
          End User
```

---

# 27. Example Pipeline Steps

For a Node.js application:

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4

  - name: Setup Node
    uses: actions/setup-node@v4

  - name: Install dependencies
    run: npm install

  - name: Run tests
    run: npm test

  - name: Build application
    run: npm run build
```

Docker build:

```yaml
- name: Build Docker image
  run: docker build -t myapp .
```

---

# 28. GitHub Actions + Docker + Kubernetes

A common DevOps architecture:

```text
                    CI
                     |
Developer ──push──> GitHub
                     |
                     v
              GitHub Actions
                     |
          +----------+----------+
          |                     |
          v                     v
        Build                  Test
          |                     |
          +----------+----------+
                     |
                     v
               Docker Build
                     |
                     v
              Docker Registry
                     |
                     v
                    CD
                     |
                     v
                Kubernetes
                     |
                     v
               Application
                     |
                     v
                 End User
```

---

# 29. GitHub Actions + Argo CD + Kubernetes

A GitOps-style architecture:

```text
Developer
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +---- Build
    |
    +---- Test
    |
    +---- Docker Image
    |
    v
Container Registry
    |
    v
GitOps Repository
    |
    v
Argo CD / Flux
    |
    v
Kubernetes / EKS
    |
    v
End User
```

---

# 30. DevOps Is Not a Tool

Important interview point:

```text
DevOps ≠ Jenkins
DevOps ≠ Docker
DevOps ≠ Kubernetes
DevOps ≠ GitHub Actions
```

DevOps is a **culture, mindset, and set of practices** focused on:

* Collaboration
* Automation
* Continuous integration
* Continuous delivery
* Feedback
* Monitoring
* Reliability
* Continuous improvement

Tools help implement DevOps practices.

```text
                    DevOps
                       |
        +--------------+--------------+
        |              |              |
     Culture        Practices     Automation
                                      |
                    +-----------------+----------------+
                    |                 |                |
                 GitHub            Docker          Kubernetes
                 Actions
```

---

# 31. GitHub Actions Learning Focus

For learning, focus on GitHub Actions first:

```text
1. GitHub Actions Basics
          ↓
2. Workflow
          ↓
3. YAML
          ↓
4. Events / Triggers
          ↓
5. Jobs
          ↓
6. Steps
          ↓
7. Actions
          ↓
8. Commands
          ↓
9. Environment Variables
          ↓
10. Secrets
          ↓
11. Artifacts
          ↓
12. Docker
          ↓
13. Docker Registry
          ↓
14. Deployment
          ↓
15. Kubernetes / EKS
          ↓
16. GitOps / Argo CD
```

---

# 32. Quick Revision

```text
CI/CD
= Automating Build → Test → Package → Deploy
```

```text
GitHub Actions
= GitHub's automation platform used to implement CI/CD workflows.
```

```text
Workflow
= Complete automation process
```

```text
Job
= Group of steps
```

```text
Step
= Individual task
```

```text
Action
= Reusable pre-built automation
```

```text
run
= Execute a shell command
```

```text
uses
= Use a pre-built Action
```

```text
.github/workflows/*.yml
= Location of GitHub Actions workflow files
```

---

# 33. Final Mental Model

```text
                         DEVOPS
                            |
                            v
                     Git Repository
                            |
                         git push
                            |
                            v
                  +-------------------+
                  |  GitHub Actions    |
                  +---------+---------+
                            |
                         WORKFLOW
                            |
                            v
                           JOB
                            |
                            v
                          STEPS
                            |
                 +----------+----------+
                 |                     |
                 v                     v
              ACTION                COMMAND
             (uses:)                (run:)
                 |                     |
                 +----------+----------+
                            |
                            v
                          BUILD
                            |
                            v
                           TEST
                            |
                            v
                      Docker Build
                            |
                            v
                   Docker Registry
                            |
                            v
                         DEPLOY
                            |
                 +----------+----------+
                 |                     |
                 v                     v
               Server             Kubernetes
                                      |
                                 Argo CD / Flux
                                      |
                                      v
                                  End User
```

# 34. One-Line Interview Answer

> **GitHub Actions is a GitHub-native automation platform used to create CI/CD workflows. We can automatically build, test, package, scan, and deploy our application whenever events such as code pushes or pull requests occur.**

### Core Formula

```text
GitHub
  ↓
GitHub Actions
  ↓
Workflow
  ↓
Job
  ↓
Steps
  ↓
Actions / Commands
  ↓
Build → Test → Docker → Deploy
  ↓
Server / Kubernetes
  ↓
End User
```

