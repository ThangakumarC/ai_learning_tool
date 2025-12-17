from fastapi import FastAPI
from pydantic import BaseModel
from ai.predict import predict_completion
from ai.difficulty import calculate_chapter_difficulty
from ai.insights import generate_insights

app = FastAPI(title="AI Learning Tool")

class StudentData(BaseModel):
    student_id: str
    course_id: str
    chapter: int
    time_spent: float
    score: float
    completion_status: int

@app.post("/analyze")
def analyze_student(data: StudentData):
    completion_prediction, risk_flag = predict_completion(
        data.time_spent,
        data.score
    )
    avg_time_spent = data.time_spent / 100
    avg_score = data.score / 100

    dropout_rate = 0.4 if data.completion_status == 0 else 0.15
    if risk_flag == "HIGH":
        dropout_rate += 0.1

    difficulty_score, chapter_label = calculate_chapter_difficulty(
        avg_time_spent,
        avg_score,
        dropout_rate
    )

    insights = generate_insights(
        data.score,
        data.time_spent,
        risk_flag,
        chapter_label
    )
    return {
        "student_id": data.student_id,
        "completion_status": data.completion_status,
        "completion_prediction": completion_prediction,
        "risk_flag": risk_flag,
        "chapter_difficulty": chapter_label,
        "difficulty_score": difficulty_score,
        "insights": insights
    }