# 🧠 AI Image Analyzer (Serverless AWS Project)

A serverless AI Image Analyzer built using **AWS cloud services**.
This project demonstrates an event-driven architecture where images uploaded to S3 automatically trigger processing via Lambda, and results can be retrieved using a RESTful GET API endpoint.

---

## 🚀 Project Overview

This application allows users to:

* Upload images to an S3 bucket
* Automatically trigger a Lambda function on upload
* Process image metadata
* Monitor execution logs via CloudWatch
* Retrieve analysis results through an HTTP API (GET request)

The project is built entirely using AWS managed services — no servers required.

---

## 🏗️ Architecture

### AWS Services Used

* **Amazon S3** – Stores uploaded images and triggers events
* **AWS Lambda** – Processes image data
* **Amazon CloudWatch** – Logs and monitoring
* **Amazon API Gateway** – Provides HTTP GET endpoint

---

## 🔄 Application Workflow

1. User uploads image to S3 bucket
2. S3 triggers Lambda function automatically
3. Lambda processes the image and generates response
4. Logs are stored in CloudWatch
5. User calls GET endpoint to retrieve image analysis result

---

## 📊 Architecture Flow Diagram

```
<img width="1425" height="407" alt="image" src="https://github.com/user-attachments/assets/5bf5a721-85c8-49d6-b865-1ffb0f8e6a13" />

---


## 🌐 API Endpoint

### GET Request

```
GET /analyze?image_name=sample.jpg
```

### Example Response

```json
{
  "image_name": "sample.jpg",
  "status": "processed",
  "message": "Image analyzed successfully"
}
```



## 📊 Monitoring

All Lambda execution logs can be viewed in:

```
/aws/lambda/<your-function-name>
```

via Amazon CloudWatch.

---

## 🔐 Security Considerations

* IAM role with least privilege access
* Secure S3 bucket policy
* API Gateway request throttling
* CloudWatch logging enabled

---

## 📈 Future Improvements

* Integrate AI detection using Amazon Rekognition
* Store processed results in DynamoDB
* Add authentication using Cognito
* Implement CI/CD pipeline
* Add POST API for direct image upload

---


