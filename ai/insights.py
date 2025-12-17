def generate_insights(score, time_spent, risk_flag, chapter_label):
    insights = []

    if score < 50:
        insights.append("Low assessment score detected")

    if time_spent < 20:
        insights.append("Low engagement time mentioned")

    if risk_flag == "HIGH":
        insights.append("Student is at high risk of dropping out")

    if chapter_label == "HARD":
        insights.append("Chapter difficulty is high, review content")

    return insights
