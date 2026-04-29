# Question 3: FastAPI Iris Classifier Deployment

## Objective
Build and deploy a machine learning web API using FastAPI and scikit-learn. The API serves a Decision Tree Classifier trained on the Iris dataset and predicts the flower class based on sepal and petal measurements.

## Deployed Application
- Live URL: https://khusbupandey-iris-api.hf.space


## Directory Structure
q3/
├── app.py             # Main FastAPI application and ML logic
├── Dockerfile         # Container configuration for Hugging Face Spaces
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

## Tech Stack
- Framework: FastAPI
- Machine Learning: scikit-learn (DecisionTreeClassifier)
- Data Handling: NumPy
- Server: Uvicorn
- Deployment Platform: Hugging Face Spaces (Docker)

## Local Setup & Execution

1. Install Dependencies:
   pip install -r requirements.txt

2. Run the Server:
   uvicorn app:app --host 0.0.0.0 --port 8000

3. Test Locally (in browser):
   http://localhost:8000/predict?sl=6.6&sw=2.3&pl=5.1&pw=1.7

## API Documentation

1. Health Check
- URL: /health
- Method: GET
- Success Response: {"status": "ok"}

2. Prediction Endpoint
- URL: /predict
- Method: GET
- Query Parameters:
  - sl (float): Sepal Length
  - sw (float): Sepal Width
  - pl (float): Petal Length
  - pw (float): Petal Width
- Expected Response: {"prediction": 1, "class_name": "versicolor"}

## Deployment Notes (Hugging Face)
This application is deployed on Hugging Face Spaces using a custom Docker container.
- Base Image: python:3.9
- Port Binding: Hugging Face requires the application to listen on port 7860.
- Command: CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]