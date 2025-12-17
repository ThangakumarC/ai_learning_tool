# AI Learning Intelligence Tool

## Project Overview

The **AI Learning Intelligence Tool** is a backend, API-based AI system designed to assist mentors and administrators in monitoring learners’ progress, predicting course completion, identifying at-risk students, and detecting difficult chapters. The tool integrates machine learning with rule-based analytics and exposes its functionality via a FastAPI service to provide interpretable insights for decision-making.


## Features

- **Course Completion Prediction**: Predicts whether a student is likely to complete a course (Binary Classification).  
- **Early Risk Detection**: Flags students at risk of dropping out based on engagement and performance.  
- **Chapter Difficulty Detection**: Identifies challenging chapters using dropout rate, time spent, and assessment scores.  
- **Insight Generation**: Provides human-readable insights such as high-risk students, key factors affecting completion, and chapters needing improvement.


## AI System Architecture

The system follows a modular architecture:
```
      API Input (JSON)
            ↓
Data Ingestion (FastAPI + Pydantic validation)
            ↓
Preprocessing (normalize time_spent and score)
            ↓
Feature Engineering (time_spent, score for ML; dropout_rate for analytics)
            ↓
ML Model Inference (predict course completion)
            ↓
Analytics & Insights (chapter difficulty, risk flags, human-readable insights)
            ↓
    JSON Output / Report
```

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Thangakumarc/ai_learning_tool.git
cd ai_learning_tool
```
2. **Create virtual environment**
```bash 
python -m venv env
source env/bin/activate   # Linux / Mac
env\Scripts\activate      # Windows
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the API**
```bash
uvicorn app.main:app --reload
```
5. **Access API Documentation**
After running the application locally, interactive API documentation
will be available at:  http://127.0.0.1:8080/docs

## Input Format

Input must be sent as JSON to /analyze endpoint:
```
{
  "student_id": "S001",
  "course_id": "C01",
  "chapter": 3,
  "time_spent": 15,
  "score": 45,
  "completion_status": 0
}
```
**Field Description:**

| Field             | Type   | Description                                                         |
|------------------|--------|---------------------------------------------------------------------|
| student_id       | string | Unique student identifier                                           |
| course_id        | string | Course identifier                                                   |
| chapter          | int    | Sequential chapter number                                           |
| time_spent       | float  | Time spent on chapter (minutes)                                     |
| score            | float  | Assessment score                                                    |
| completion_status| int    | Historical completion status (1 = completed, 0 = dropped)           |

## Output Format
```
{
  "student_id": "S001",
  "completion_status": 0,
  "completion_prediction": "NOT LIKELY",
  "risk_flag": "HIGH",
  "chapter_difficulty": "HARD",
  "difficulty_score": 0.63,
  "insights": [
    "Low assessment score detected",
    "Low engagement time mentioned",
    "Student is at high risk of dropping out",
    "Chapter difficulty is high, review content",
    "Student has previously dropped out of this course"
  ]
}
```
## AI Model & Feature Details

Model: Logistic Regression

Features used for ML: time_spent, score

Rule-based features: dropout_rate, chapter order, difficulty_score

Reasoning: Hybrid approach ensures both predictive power (ML) and interpretability (rule-based insights)

## Live Demo

The AI Learning Intelligence Tool is deployed on Render and can be accessed here:

https://ai-learning-tool-6ygd.onrender.com/docs

The link provides interactive API documentation where users can
test the AI endpoints directly.

## Sample Input
```
{
  "student_id": "S101",
  "course_id": "C01",
  "chapter": 4,
  "time_spent": 15,
  "score": 35,
  "completion_status" : 1
}
```
## Output 
```
{
  "student_id": "S101",
  "completion_status": 1,
  "completion_prediction": "NOT LIKELY",
  "risk_flag": "HIGH",
  "chapter_difficulty": "EASY",
  "difficulty_score": 0.34,
  "insights": [
    "Low assessment score detected",
    "Low engagement time mentioned",
    "Student is at high risk of dropping out"
  ]
}
```
## AI Usage Disclosure

This project was developed in compliance with the assessment’s AI usage policy.

A machine learning model is used to predict course completion. Rule-based analytics are used to compute chapter difficulty and generate human-readable insights. No sensitive or real user data is used; all datasets are synthetic and created for demonstration purposes. Predictions and insights are intended solely for learning and evaluation, not for real-world decision-making.

## Use of AI Tools

This project was developed with the assistance of the AI tool ChatGPT, which was used to: Understand the problem statement and assessment requirements, Clarify machine learning concepts and system architecture, Guide deployment steps and API structuring, Review code structure for correctness and clarity.

All AI-generated suggestions were manually reviewed, understood, and adapted before implementation. Core application logic, system integration, and decision-making rules were implemented independently to ensure correctness and transparency, in accordance with the assessment guidelines.
