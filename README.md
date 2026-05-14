# SIT707 7.2H GCP CI/CD Project

## Application

SIT707 Quality Tracker is a modular Flask web application designed to demonstrate software quality monitoring, automated testing, containerisation, and cloud deployment through Google Cloud Platform CI/CD services.

## Features

- Homepage with software quality summary
- Dashboard for adding test evidence records
- Backend validation and summary calculation logic
- Health API endpoint for deployment verification
- Pytest automated test suite
- Right-BICEP high-level testing
- TDD red-green validation improvement
- Dockerfile for container deployment
- Cloud Build configuration for CI/CD
- Cloud Run deployment target

## Local run

1. Create virtual environment.
2. Activate virtual environment.
3. Install dependencies from requirements.txt.
4. Run python run.py.
5. Open http://127.0.0.1:8080.

## Run tests

Run pytest -v.

## GCP CI/CD process

The cloudbuild.yaml file defines the following pipeline stages:

1. Install Python dependencies.
2. Run the pytest automated test suite.
3. Build a Docker container image.
4. Push the image to Artifact Registry.
5. Deploy the image to Cloud Run.

## Deployment target

- Runtime: Cloud Run
- Region: australia-southeast1
- Image registry: Artifact Registry
- CI/CD service: Google Cloud Build
- Source repository: GitHub

Trigger verification: GitHub push should start the Cloud Build CI/CD pipeline.
