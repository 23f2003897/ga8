# Question 4: Sentiment Analysis ML API

## Objective
Deploy a pre-trained machine learning model as a REST API on Hugging Face Spaces. The API performs sentiment analysis using the Hugging Face transformers library and is built with FastAPI.

## Deployed Application
- Live URL: [https://khusbupandey-sentiment-api.hf.space](https://khusbupandey-sentiment-api.hf.space)
- Platform: Hugging Face Spaces (Docker SDK)

## Tech Stack
- Framework: FastAPI
- Machine Learning: Hugging Face transformers
- Server: Uvicorn
- Containerization: Docker

## API Documentation

### Predict Sentiment Endpoint
- URL: /predict
- Method: POST
- Description: Analyzes the emotional sentiment of the provided text.

Request Body (JSON):
{
  "text": "I love how easy this API was to build!"
}

Response (JSON):
{
  "label": "POSITIVE",
  "score": 0.9998
}

## How to Test
Because this is a POST endpoint, it cannot be tested by pasting the URL into a web browser. You can test it via PowerShell using the following command:

Invoke-RestMethod -Uri "[https://khusbupandey-sentiment-api.hf.space/predict](https://khusbupandey-sentiment-api.hf.space/predict)" -Method Post -Body '{"text": "I am so happy this works!"}' -ContentType "application/json"