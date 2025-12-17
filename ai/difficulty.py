def calculate_chapter_difficulty(
    avg_time_spent: float,
    avg_score: float,
    dropout_rate: float
):
    """
    Returns difficulty score and label
    """

    difficulty_score = (
        dropout_rate * 0.4 +
        avg_time_spent * 0.3 +
        (1 - avg_score) * 0.3
    )

    if difficulty_score > 0.6:
        label = "HARD"
    elif difficulty_score > 0.4:
        label = "MEDIUM"
    else:
        label = "EASY"

    return round(difficulty_score, 2), label
