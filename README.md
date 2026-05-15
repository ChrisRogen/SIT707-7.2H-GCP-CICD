# SIT707 7.2HD GCP CI/CD Project

## Application

SIT707 Quality Tracker is a modular Flask web application designed to demonstrate software quality monitoring, automated testing, containerisation, and cloud deployment through Google Cloud Platform CI/CD services.

## Live Project Links

Live Cloud Run application:

```text
https://sit707-quality-tracker-7ngjjlurqq-ts.a.run.app
```

Live status page:

```text
https://sit707-quality-tracker-7ngjjlurqq-ts.a.run.app/status
```

Health API endpoint:

```text
https://sit707-quality-tracker-7ngjjlurqq-ts.a.run.app/health
```

GitHub repository:

```text
https://github.com/ChrisRogen/SIT707-7.2H-GCP-CICD
```

## Main Features

- Flask web application with modular structure.
- Homepage showing software quality summary.
- Dashboard for adding and viewing test evidence records.
- Backend validation for test name, module name, and status.
- Summary calculation for total, passed, failed, blocked, and pass rate.
- JSON health API endpoint at `/health`.
- Styled health status page at `/status`.
- Automated pytest test suite.
- Right-BICEP style high-level testing.
- TDD red-green testing evidence.
- Dockerfile for containerised deployment.
- Cloud Build configuration using `cloudbuild.yaml`.
- Artifact Registry Docker image storage.
- Cloud Run deployment.
- GitHub push trigger for automated CI/CD execution.

## Application Routes

| Route | Purpose |
|---|---|
| `/` | Homepage showing software quality summary cards |
| `/dashboard` | Dashboard for adding and viewing test evidence records |
| `/health` | Raw JSON health API endpoint |
| `/status` | Styled health status page for deployment verification |

## Project Folder Structure

```text
SIT707-7.2H-GCP-CICD/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── services.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── index.html
│       └── status.html
├── tests/
│   ├── test_services.py
│   ├── test_routes.py
│   ├── test_quality_tracker_high_level.py
│   └── test_intentional_failure.py
├── .dockerignore
├── .gcloudignore
├── .gitignore
├── cloudbuild.yaml
├── Dockerfile
├── pytest.ini
├── README.md
├── requirements.txt
└── run.py
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application framework |
| pytest | Automated testing framework |
| Gunicorn | Production WSGI server |
| Docker | Containerisation |
| Git | Local version control |
| GitHub | Remote source code repository |
| Google Cloud SDK | Command-line access to Google Cloud |
| Google Cloud Build | CI/CD pipeline execution |
| Google Artifact Registry | Docker image storage |
| Google Cloud Run | Serverless container hosting |
| Google IAM | Permission management for deployment |

---

# Local Replication Instructions

Follow these steps to run the project on another local machine.

## Step 1: Install Required Software

Install the following tools:

```text
Python 3.12 or later
Git
Google Chrome or another web browser
Visual Studio Code or another code editor
```

Optional tools for cloud deployment:

```text
Google Cloud SDK
Docker Desktop
Google Cloud account with billing enabled
```

## Step 2: Clone the GitHub Repository

Open PowerShell or Terminal and run:

```powershell
git clone https://github.com/ChrisRogen/SIT707-7.2H-GCP-CICD.git
cd SIT707-7.2H-GCP-CICD
```

## Step 3: Create a Python Virtual Environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

For macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, the terminal should show the virtual environment name, for example:

```text
(.venv)
```

## Step 4: Install Project Dependencies

Run:

```powershell
pip install -r requirements.txt
```

Expected main dependencies:

```text
Flask
pytest
gunicorn
```

## Step 5: Run Automated Tests

Run:

```powershell
pytest -v
```

Expected result:

```text
23 passed
```

This confirms that the application logic, Flask routes, form validation, health endpoint, status page, and high-level quality tracker tests are working correctly.

## Step 6: Run the Application Locally

Run:

```powershell
python run.py
```

The application should start on:

```text
http://127.0.0.1:8080
```

Open the following pages in a browser:

Homepage:

```text
http://127.0.0.1:8080
```

Dashboard:

```text
http://127.0.0.1:8080/dashboard
```

Health API:

```text
http://127.0.0.1:8080/health
```

Styled status page:

```text
http://127.0.0.1:8080/status
```

## Step 7: Stop the Local Server

Press:

```text
CTRL + C
```

in the terminal where Flask is running.

---

# How the Application Works

The application starts from:

```text
run.py
```

`run.py` creates the Flask application using the application factory inside:

```text
app/__init__.py
```

The route logic is defined in:

```text
app/routes.py
```

The backend service logic is defined in:

```text
app/services.py
```

The application stores sample test records in memory and calculates a quality summary. The dashboard form allows users to add a test evidence record using:

```text
Test name
Module name
Status: Pass, Fail, or Blocked
```

The backend validates the submitted data before adding the record. Empty values, whitespace-only values, and invalid status values are rejected.

The summary output includes:

```text
Total tests
Passed tests
Failed tests
Blocked tests
Pass rate
```

---

# Testing Strategy

The project uses pytest for automated testing.

The test suite covers:

| Test Area | Description |
|---|---|
| Unit testing | Tests backend validation and summary calculation functions |
| Route testing | Tests Flask routes such as `/`, `/dashboard`, `/health`, and `/status` |
| Boundary testing | Tests empty and whitespace-only values |
| Error testing | Tests invalid status values and missing form values |
| Integration testing | Tests dashboard form submission through Flask test client |
| API contract testing | Tests expected JSON response from `/health` |
| Right-BICEP testing | Tests right values, boundaries, inverse relationships, cross-checking, errors, and performance |
| TDD evidence | Shows failing tests corrected into passing tests |

Important test files:

```text
tests/test_services.py
tests/test_routes.py
tests/test_quality_tracker_high_level.py
tests/test_intentional_failure.py
```

## TDD Failure and Fix Example

A boundary validation issue was identified where whitespace-only input could be accepted.

A failing test was created first:

```python
def test_boundary_whitespace_only_test_name_is_rejected():
    result = validate_test_record("   ", "Authentication", "Pass")
    assert result["valid"] is False
```

The validation logic was then improved by stripping whitespace before checking the input:

```python
test_name = str(test_name).strip()
module_name = str(module_name).strip()
status = str(status).strip()
```

After the fix, the full test suite passed.

---

# Docker Instructions

The project includes a Dockerfile for containerised execution.

## Build Docker Image Locally

```powershell
docker build -t sit707-quality-tracker .
```

## Run Docker Container Locally

```powershell
docker run -p 8080:8080 sit707-quality-tracker
```

Then open:

```text
http://127.0.0.1:8080
```

---

# Google Cloud Deployment Overview

The project was deployed using the following Google Cloud services:

| GCP Service | Purpose |
|---|---|
| Cloud Build | Runs tests, builds Docker image, pushes image, and deploys to Cloud Run |
| Artifact Registry | Stores Docker container images |
| Cloud Run | Hosts the containerised Flask application |
| IAM | Grants permissions for Cloud Build and Cloud Run deployment |
| Google Cloud SDK | Allows deployment commands from the local terminal |

---

# Google Cloud Replication Instructions

Use your own Google Cloud project if you want to replicate the deployment.

## Step 1: Login to Google Cloud CLI

```powershell
gcloud auth login
```

## Step 2: List Available Projects

```powershell
gcloud projects list
```

## Step 3: Select Your Project

Replace `YOUR_PROJECT_ID` with your own GCP project ID:

```powershell
gcloud config set project YOUR_PROJECT_ID
```

Check the active project:

```powershell
gcloud config list
```

## Step 4: Confirm Billing Is Enabled

```powershell
gcloud billing projects describe YOUR_PROJECT_ID
```

Expected value:

```text
billingEnabled: true
```

Cloud deployment will not work properly unless billing is enabled.

## Step 5: Enable Required Google Cloud APIs

```powershell
gcloud services enable cloudbuild.googleapis.com run.googleapis.com artifactregistry.googleapis.com iamcredentials.googleapis.com
```

Verify enabled services:

```powershell
gcloud services list --enabled --format="table(config.name,title)"
```

The following services should be enabled:

```text
cloudbuild.googleapis.com
run.googleapis.com
artifactregistry.googleapis.com
iamcredentials.googleapis.com
```

## Step 6: Create Artifact Registry Repository

This project uses the region:

```text
australia-southeast1
```

Create the Docker repository:

```powershell
gcloud artifacts repositories create sit707-cicd-repo --repository-format=docker --location=australia-southeast1 --description="Docker repository for SIT707 CI CD project"
```

Verify the repository:

```powershell
gcloud artifacts repositories list --location=australia-southeast1
```

## Step 7: Configure IAM Permissions

Cloud Build needs permission to push images and deploy to Cloud Run.

In the Google Cloud Console, check IAM permissions for the Cloud Build and Compute service accounts.

Required roles may include:

```text
Cloud Build Editor
Cloud Run Admin
Artifact Registry Writer
Service Account User
Logging Writer
Storage Admin
```

For a learning project, these roles allow Cloud Build to build, push, and deploy the application. In a production project, permissions should be reduced using least-privilege access.

## Step 8: Submit Cloud Build Manually

Run this command from the project folder:

```powershell
gcloud builds submit --config cloudbuild.yaml .
```

Expected result:

```text
STATUS: SUCCESS
```

## Step 9: Check Cloud Run Service

```powershell
gcloud run services describe sit707-quality-tracker --region=australia-southeast1 --format="table(metadata.name,status.url,status.latestReadyRevisionName)"
```

The output should show:

```text
Service name
Cloud Run URL
Latest ready revision
```

Open the Cloud Run URL in a browser.

---

# Cloud Build Pipeline

The `cloudbuild.yaml` file performs the following steps:

1. Install Python dependencies.
2. Run pytest.
3. Build Docker image.
4. Push Docker image to Artifact Registry.
5. Deploy Docker image to Cloud Run.

The pipeline uses:

```yaml
_REGION: australia-southeast1
_REPOSITORY: sit707-cicd-repo
```

If a different region or repository name is used, update the `cloudbuild.yaml` file before running Cloud Build.

The image tag uses:

```text
$BUILD_ID
```

This was used because `$BUILD_ID` works correctly during manual Cloud Build submission.

---

# GitHub Trigger Setup

A Cloud Build trigger was configured so that a push to the GitHub `main` branch automatically starts the CI/CD pipeline.

Trigger configuration:

| Field | Value |
|---|---|
| Trigger name | `sit707-quality-tracker-main-trigger` |
| Repository | `ChrisRogen/SIT707-7.2H-GCP-CICD` |
| Event | Push to branch |
| Branch | `main` |
| Build config file | `cloudbuild.yaml` |
| Status | Enabled |

## Test the Trigger

A small README update can be used to test the trigger:

```powershell
Add-Content .\README.md "`nTrigger verification: GitHub push should start the Cloud Build CI/CD pipeline."
git add README.md
git commit -m "Trigger Cloud Build from GitHub push"
git push
```

After pushing, go to:

```text
Google Cloud Console > Cloud Build > History
```

A new build should appear automatically. Wait until the build status becomes:

```text
SUCCESS
```

---

# Issues Faced and Fixes

| Issue | Cause | Fix |
|---|---|---|
| GCP project creation failed | Cloud Resource Manager quota rate limit | Retried project creation and continued setup |
| Billing disabled on first project | Initial project did not have billing enabled | Switched to a billing-enabled GCP project |
| `gcloud` not recognised in PowerShell | Google Cloud SDK path was not available in the active terminal | Added the Google Cloud SDK path to the PowerShell session |
| pytest configuration error | Invalid leading character in `pytest.ini` | Recreated `pytest.ini` with clean ASCII content |
| Boundary validation failed | Whitespace-only values were accepted | Added `.strip()` before validation |
| Intentional CI test failed | Expected pass rate was intentionally set incorrectly for evidence | Corrected expected value and restored passing test suite |
| Cloud Build image tag failed | `$SHORT_SHA` was unavailable in manual build | Changed image tag to `$BUILD_ID` |
| Raw health endpoint looked empty | `/health` returned JSON, not HTML | Kept `/health` as API and added styled `/status` page |
| GitHub trigger did not show repository at first | GitHub repository was not connected to Cloud Build | Installed Google Cloud Build GitHub App and selected the repository |
| GCP account and GitHub account were different | Cloud project and GitHub repository used different accounts | Connected the GitHub account that owned the repository while using the selected GCP project |

---

# Current Limitations

This version is a learning and demonstration project.

Current limitations:

- Test records are stored in memory.
- New dashboard records are not permanently saved after restart or redeployment.
- The deployed Cloud Run service allows unauthenticated access for demonstration.
- No user login or role-based access control is implemented.
- No database is connected.
- No file upload feature is currently implemented.
- No charts or export reports are currently implemented.

---

# Future Improvements

Future improvements can include:

- Upload Excel or CSV test reports through the dashboard.
- Automatically parse uploaded spreadsheet test reports.
- Generate a detailed test report summary from uploaded files.
- Store test records in a database such as Cloud SQL or Firestore.
- Add user authentication.
- Add role-based access control.
- Add charts for pass rate and module-level quality trends.
- Add export to PDF or Excel.
- Add email notification after build success or failure.
- Add Cloud Monitoring dashboard.
- Add container image security scanning.
- Add GitHub pull request checks before merge.
- Add separate staging and production environments.

## Planned Feature: Upload Excel Test Report

A useful future feature would be an upload option in the dashboard where users can upload an Excel or CSV test report.

The uploaded file could contain columns such as:

```text
test_name
module_name
status
created_at
tester
priority
comments
```

The application could read the spreadsheet, validate each row, and generate:

```text
Total tests
Passed tests
Failed tests
Blocked tests
Pass rate
Module-wise summary
High-risk failed test list
```

This would improve the project because testers could upload real test reports instead of manually entering each test record. It would also make the application more realistic for software quality reporting.

---

# Video Demonstration Guide

A video explaining how to replicate this project should include:

1. Open the GitHub repository.
2. Explain the project purpose.
3. Show the project folder structure.
4. Clone the repository.
5. Create and activate the virtual environment.
6. Install dependencies.
7. Run `pytest -v`.
8. Explain the 23 passing tests.
9. Run `python run.py`.
10. Open the local homepage.
11. Open the dashboard.
12. Add or explain a test record.
13. Open `/health`.
14. Open `/status`.
15. Explain Dockerfile and `cloudbuild.yaml`.
16. Explain Cloud Build, Artifact Registry, and Cloud Run.
17. Show Cloud Build history.
18. Show Cloud Run live URL.
19. Show GitHub trigger configuration.
20. Explain that pushing to GitHub automatically starts Cloud Build.
21. Explain issues faced and how they were fixed.
22. Explain future improvement: Excel test report upload and automatic summary generation.

---

# Final Outcome

This project demonstrates a complete CI/CD workflow for a Flask web application. The application was developed locally, tested with pytest, containerised with Docker, deployed using Google Cloud Build and Cloud Run, and automated through a GitHub push trigger.

The final working pipeline proves that a code change pushed to GitHub can automatically start a Cloud Build process, run tests, build a Docker image, store it in Artifact Registry, and deploy the latest version to Cloud Run.
