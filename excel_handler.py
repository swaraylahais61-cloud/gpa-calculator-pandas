"""
Read academic excel file and return dataframes.
"""

import pandas as pd


def read_academic_excel(file_path):

    # Read Subjects sheet
    subjects_df = pd.read_excel(
        file_path,
        sheet_name="Subjects",
        engine="openpyxl"
    )

    # Read Students sheet
    students_df = pd.read_excel(
        file_path,
        sheet_name="Students",
        engine="openpyxl"
    )

    # Read RawScores sheet
    raw_scores_df = pd.read_excel(
        file_path,
        sheet_name="RawScores",
        engine="openpyxl"
    )

    print("Excel loaded successfully!")

    return subjects_df, students_df, raw_scores_df

# Run this file directly for testing

if __name__ == "__main__":

    subjects_df, students_df, raw_scores_df = read_academic_excel(
        "academic_data.xlsx"
    )

    print("\nSubjects")
    print(subjects_df)

    print("\nStudents")
    print(students_df)

    print("\nRaw Scores")
    print(raw_scores_df)

