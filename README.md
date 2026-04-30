# GA8: MLOps Concepts, Code Quality, and Cloud Deployment

## Overview
This repository contains the complete solutions for the GA8 assignment. It demonstrates a progression from basic version control and code formatting to advanced pre-commit hooks, CI/CD workflows, and containerized cloud deployments.

## Repository Structure
* **`q1/`** - **`q5/`**: Foundational Python scripts demonstrating automated formatting, linting, and code quality enforcement using `ruff`.
* **`q6/`**: Shell scripting for environment setup and automated tasks.
* **`q7/`**: Implementation of Git hooks (specifically `pre-commit`) to ensure code quality standards are met before any code is checked into the repository.
* **`q8/`**: Documentation and analysis of core MLOps concepts and quiz validations.
* **`q9/`**: **Cloud Compute Service**
  * A containerized FastAPI application calculating arithmetic sums, products, and SHA-256 verification hashes.
  * Packaged via Docker and deployed live as a serverless container application.

## Key Technologies Used
* **Languages:** Python 3.11, Bash/Shell
* **Frameworks:** FastAPI, Uvicorn, Pydantic
* **Code Quality:** Ruff, pre-commit hooks
* **DevOps & Cloud:** Docker, GitHub version control, Serverless Cloud Containers (Azure Container Apps / GCP Cloud Run)

## Deployment (Question 9)
The final compute service for Question 9 is fully containerized and deployed publicly. It exposes a `/health` endpoint for status checks and a `/compute` endpoint that processes JSON payloads to return verified computational hashes based on assigned seed values.
