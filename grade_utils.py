"""
grade_utils.py
Handles academic score conversions.
"""
import pandas as pd

def convert_score_to_letter_grade(score):
    """Convert a numeric score to a letter grade safely handling floats and NaN."""
    # Handle missing/empty data from Pandas
    if score is None or pd.isna(score):
        return "E"

    try:
        score_value = float(score)
    except (ValueError, TypeError):
        return "E"

    # Strict thresholds using continuous ranges to handle decimal scores
    if score_value >= 85:
        return "A"
    elif score_value >= 70:
        return "B"
    elif score_value >= 60:
        return "C"
    elif score_value >= 50:
        return "D"
    else:
        return "E"


def convert_letter_grade_to_point(letter_grade):
    """Convert letter grade to numerical GPA points using a fast dictionary look-up."""
    # Convert to string and strip spaces just in case
    grade = str(letter_grade).strip().upper() if letter_grade else "E"
    
    # Fast lookup dictionary
    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "E": 0.0
    }
    
    return grade_points.get(grade, 0.0)

