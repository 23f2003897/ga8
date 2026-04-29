# Question 5: Docker Multi-stage Build

## Objective
Build a Docker image that trains a GradientBoostingClassifier on the breast_cancer dataset, then prints a verification hash and accuracy. The image is optimized using a multi-stage build to ensure a minimal final runtime footprint.

## Execution Results
- Accuracy: 0.9649
- Verify Hash: 9c773484d572
- Final Image Size: 186MB

## Assignment Submission String
0.9649,9c773484d572,186

## Tech Stack
- Language: Python 3.11
- ML Library: scikit-learn
- Containerization: Docker (Multi-stage)

## How to Run
1. Build the image:
   docker build -t mlops-verify .

2. Run the container to view results:
   docker run --rm mlops-verify
