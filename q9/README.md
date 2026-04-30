# Question 9: GCP Cloud Run Compute Service

## Objective
Deploy a containerized FastAPI compute service to Google Cloud Platform (GCP) Cloud Run.

## Application Logic
The API exposes two endpoints:
- `GET /health`: Returns a simple status check.
- `POST /compute`: Accepts integers `A` and `B`, calculates the sum and product, and returns a verified SHA-256 hash.

## Deployment Details
- **Platform:** GCP Cloud Run
- **Framework:** FastAPI (Python 3.11)
- **Parameters Used:** `A=6`, `B=13`
- **Expected Output Hash:** `9f719abad3`

## Execution
This service uses Google Cloud Build to bypass local Docker daemon requirements, packaging the image securely in the Google Container Registry before deploying as an unauthenticated managed service on Cloud Run.
