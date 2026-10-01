# GitHub Actions and CI/CD Pipeline – DevOps Beginner Notes

## 1. What is CI/CD?

**CI/CD** is a software-development practice that automates how code is built, tested, packaged, and delivered.

- **CI – Continuous Integration:** Developers frequently push code changes to a shared repository. Automated jobs can build the application and run tests so problems are found earlier.
- **CD – Continuous Delivery:** After successful checks, a change is kept ready for release. Deployments may require a manual approval.
- **CD – Continuous Deployment:** Every change that passes the required checks is automatically deployed to the target environment.

> CI/CD makes the software delivery process repeatable and reduces manual work. It does not replace code review, security controls, monitoring, or good engineering practices.

## 2. What is GitHub Actions?

**GitHub Actions** is GitHub's automation and CI/CD platform. It runs automated workflows in response to events in a GitHub repository, such as a push, pull request, scheduled time, or manual trigger.

A workflow is defined in a YAML file stored in the repository under:

```text
.github/workflows/
```

For example:

```text
.github/workflows/hello.yml
```

GitHub Actions became generally available on **November 13, 2019**, after its public beta announcement in August 2019.

### Why use GitHub Actions?

- **GitHub integration:** Workflows live alongside source code and can run on pushes and pull requests.
- **Automation:** Build, test, package, publish, and deployment tasks can run without repeating them manually.
- **Reusable actions:** Use existing actions from the GitHub Marketplace or create your own.
- **Flexible runners:** Run jobs on GitHub-hosted runners or supported self-hosted runners.
- **Visibility:** View workflow runs, job logs, and failures in the repository's Actions tab.
- **Deployment controls:** Use environments, approvals, and secrets to manage releases.

GitHub Actions is especially convenient when your source code and pull-request workflow already use GitHub.

## 3. CI/CD pipeline overview

A typical application pipeline can look like this:

```text
       Developer
           |
           | git push / Pull Request
           v
     GitHub Repository
           |
           | Repository event triggers workflow
           v
      GitHub Actions
           |
           v
     Build Application
           |
           v
       Run Tests
           |
           v
   Build Docker Image
           |
           v
  Publish Image to Registry
           |
           v
   Deploy to Server / Kubernetes
           |
           v
     Verify Deployment
           |
           v
        End User
```

**Important:** This is an example flow, not a mandatory sequence. A project may test before building an image, skip Docker, deploy to a virtual machine, or deploy to Kubernetes. A failed required job should prevent later release jobs from running.

## 4. GitHub Actions concepts

The main structure is:

```text
Workflow
  └── Jobs
       └── Steps
            ├── Run a shell command
            └── Use a predefined or custom Action
```

| Concept | Meaning |
|---|---|
| **Workflow** | The complete automated process, defined in a YAML file. |
| **Event / Trigger** | The event that starts a workflow, such as `push`, `pull_request`, or `workflow_dispatch`. |
| **Job** | A group of steps executed on a runner. Jobs run in parallel by default unless dependencies are defined with `needs`. |
| **Runner** | The machine that executes a job, such as `ubuntu-latest` or a self-hosted runner. |
| **Step** | An individual task inside a job. Steps run in order within that job. |
| **Command (`run`)** | A shell command or script executed by a step. |
| **Action (`uses`)** | A reusable unit of automation, referenced by name and version or commit. |
| **Workflow file** | A YAML file saved in `.github/workflows/`. |

### Commands versus Actions

A `run` step executes commands directly:

```yaml
- name: Show current directory
  run: pwd
```

A `uses` step invokes a reusable action:

```yaml
- name: Check out repository
  uses: actions/checkout@v4
```

An action is not simply a command written in YAML; it is a reusable automation component. Workflows can combine shell commands and actions.

## 5. Create your first GitHub Actions workflow

### Step 1 – Create a GitHub repository

1. Sign in to GitHub.
2. Select **New repository**.
3. Enter a repository name, for example:

   ```text
   github-action-practice
   ```

4. Choose the visibility you want.
5. Optionally select **Add a README file**.
6. Create the repository.

### Step 2 – Create the workflow directory

In the repository, create this directory structure:

```text
github-action-practice/
├── README.md
└── .github/
    └── workflows/
        └── hello.yml
```

The directory name must be `.github/workflows` (plural: `workflows`). GitHub discovers workflow YAML files placed there.

### Step 3 – Add `hello.yml`

Create `.github/workflows/hello.yml` with the following content:

```yaml
name: Hello GitHub Actions

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

jobs:
  hello:
    name: Hello Job
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Display a message
        run: echo "Hello from GitHub Actions!"

      - name: Show repository files
        run: ls -la
```

> If your repository uses `master` instead of `main`, change the branch names in the trigger configuration to `master`.

### Step 4 – Understand the YAML

- `name`: The workflow's display name in the Actions tab.
- `on`: Defines the events that start the workflow.
  - `push`: Runs when commits are pushed to `main`.
  - `pull_request`: Runs for pull requests targeting `main`.
  - `workflow_dispatch`: Allows a user to start the workflow manually from GitHub.
- `jobs`: Contains one or more jobs.
- `hello`: This is the job ID; it can be chosen by the repository author.
- `runs-on`: Selects the runner environment. Here, GitHub-hosted Ubuntu is used.
- `steps`: Lists the tasks in the job, executed in order.
- `uses`: Runs a reusable action. `actions/checkout` checks out the repository so the job can access its files.
- `run`: Executes a shell command on the runner.

### Step 5 – Commit and run the workflow

1. Save the file at `.github/workflows/hello.yml`.
2. Commit the change to the repository's `main` branch.
3. Open the repository's **Actions** tab.
4. Select **Hello GitHub Actions** and open the latest run.
5. Expand the `Hello Job` steps to view their logs.

The workflow also supports manual execution through **Run workflow**, when the repository and workflow permissions allow it.

## 6. Example: a simple CI workflow for a Node.js project

The following example checks out a Node.js project, installs dependencies, and runs its test script. It assumes the repository has a `package-lock.json` file and a `test` script in `package.json`.

```yaml
name: Node.js CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out source code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test
```

This is a **CI example**: it validates code changes. It does not build or deploy a Docker image. A Docker build, image push, and deployment can be added as later jobs after the required checks pass.

## 7. Where GitHub Actions fits among CI/CD tools

GitHub Actions is one option in a broader DevOps ecosystem. Tools may overlap, and teams select them based on their source-control platform, infrastructure, compliance requirements, and existing workflows.

| Tool | General role |
|---|---|
| **GitHub Actions** | Automation and CI/CD integrated with GitHub repositories. |
| **GitLab CI/CD** | Pipeline automation integrated with GitLab repositories and its DevSecOps platform. |
| **Jenkins** | Extensible automation server commonly used for CI/CD, with a large plugin ecosystem. |
| **CircleCI** | Hosted and self-hosted CI/CD platform for building, testing, and delivery workflows. |
| **Atlassian Bamboo** | CI/CD server integrated with other Atlassian developer tools. |
| **JetBrains TeamCity** | CI/CD build and automation server. |
| **Azure DevOps Pipelines** | CI/CD pipelines within Microsoft's Azure DevOps services. |
| **AWS CodePipeline** | AWS service for orchestrating release pipelines with AWS and other integrations. |
| **Argo CD** | Kubernetes-focused GitOps continuous delivery tool that synchronizes cluster state with Git-defined configuration. |
| **Flux CD** | Kubernetes GitOps toolkit for keeping cluster state aligned with sources such as Git repositories. |

### CI versus CD and Kubernetes delivery

- GitHub Actions, GitLab CI/CD, Jenkins, CircleCI, Bamboo, TeamCity, Azure Pipelines, and AWS CodePipeline can automate build, test, and release stages, depending on configuration.
- **Argo CD and Flux CD** focus on GitOps-based delivery to Kubernetes. They are commonly used to reconcile Kubernetes resources with desired configuration stored in Git.
- These categories are not mutually exclusive. For example, GitHub Actions can build and publish a container image, while Argo CD or Flux deploys the updated application to Kubernetes.

## 8. GitHub and Microsoft

Microsoft announced its agreement to acquire GitHub in June 2018, and the acquisition was completed in October 2018. GitHub continues to support a broad developer ecosystem, including projects that use other CI/CD providers.

GitHub Actions is a GitHub product; **GitLab CI/CD is GitLab's own pipeline system**. They are alternatives for many CI tasks, but neither is simply a renamed version of the other.

## 9. DevOps is a culture and practice, not a single tool

**DevOps** brings development and operations practices together to improve collaboration, automation, feedback, reliability, and delivery.

CI/CD tools support DevOps practices, but installing a tool alone does not establish DevOps. Teams also need practices such as:

- Version control and peer review
- Automated tests and quality checks
- Infrastructure as Code
- Secure handling of credentials and permissions
- Monitoring, logging, and feedback
- Repeatable deployments and recovery plans
- Shared ownership and continuous improvement

## 10. Key takeaways

- **CI** automates integration checks such as builds and tests.
- **CD** automates delivery or deployment, with the degree of automation determined by the team's release process.
- **GitHub Actions** runs workflows defined in YAML under `.github/workflows/`.
- A workflow contains **jobs**; jobs run on **runners** and contain ordered **steps**.
- Steps can execute shell **commands** using `run` or reusable **actions** using `uses`.
- GitHub Actions can support the path from a code push to a tested artifact and deployment, but the exact pipeline depends on the project.
- Jenkins, GitLab CI/CD, CircleCI, Bamboo, TeamCity, Azure DevOps, AWS CodePipeline, Argo CD, and Flux CD are other tools in the CI/CD and delivery ecosystem.

---

**Practice task:** Create the `github-action-practice` repository, add `.github/workflows/hello.yml`, commit it, and inspect the workflow run and step logs in the **Actions** tab.
