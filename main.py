"""main.py

Entry point for the academic GPA processing assignment.
This file connects the Excel reading, grade conversion, and GPA calculation.

The code uses pandas + openpyxl (through pandas Excel support).
"""

import pandas as pd  # Import pandas for data handling

from excel_handler import read_academic_excel  # Import function to read Excel sheets
from grade_utils import (
    convert_score_to_letter_grade,  # Convert numeric score -> letter grade
    convert_letter_grade_to_point,  # Convert letter grade -> grade point
) 


def main():
    # Path to the Excel file (must be in the same folder as this project)
    file_path = "academic_data.xlsx"

    # Read all sheets from the Excel file into pandas DataFrames
    subjects_df, students_df, raw_scores_df = read_academic_excel(file_path)

    # Print the content of each DataFrame so the user can see everything clearly
    print("\n=====================") 
    print("Subjects DataFrame")
    print("=====================")
    print(subjects_df)

    print("\n====================")
    print("Students DataFrame")
    print("====================")
    print(students_df)

    print("\n====================")
    print("RawScores DataFrame")
    print("====================")
    print(raw_scores_df)

    # ------------------------------
    # Merge RawScores + Students
    # ------------------------------
    # We merge on StudentID so we can bring Student Name and Group into RawScores
    merged_df = raw_scores_df.merge(
        students_df,
        how="left",  # Keep all raw scores rows
        left_on="StudentID",  # Column in RawScores
        right_on="StudentID"  # Column in Students
    )

    # ------------------------------
    # Merge (result) + Subjects
    # ------------------------------
    # We merge on SubjectCode and also include Code from Subjects
    # Requirement says: merge using SubjectCode and Code
    merged_df = merged_df.merge(
        subjects_df,
        how="left",  # Keep all rows that already came from the raw scores
        left_on="SubjectCode",  # Column in merged_df (from RawScores)
        right_on="Code"  # Column in Subjects
    )

    # ------------------------------
    # Convert numeric Score -> Letter Grade
    # ------------------------------
    # Make a new column for letter grade
    merged_df["LetterGrade"] = merged_df["Score"].apply(convert_score_to_letter_grade)

    # ------------------------------
    # Convert LetterGrade -> Points
    # ------------------------------
    merged_df["Point"] = merged_df["LetterGrade"].apply(convert_letter_grade_to_point)

    # ------------------------------
    # Calculate WeightedPoint = Point * SKS
    # ------------------------------
    # WeightedPoint is the grade point multiplied by course credit (SKS)
    merged_df["WeightedPoint"] = merged_df["Point"] * merged_df["SKS"]

     
    # Calculate GPA per student
    # ------------------------------

    # Group the merged data by StudentID, Student Name and Group
    # This allows us to calculate totals for each student
    gpa_table = merged_df.groupby(

        ["StudentID", "Student Name", "Group"]

    ).agg(

        # Add all weighted points for each student
        TotalWeightedPoint=("WeightedPoint", "sum"),

        # Add all SKS for each student
        TotalSKS=("SKS", "sum")

    ).reset_index()


    # ------------------------------
        # ------------------------------
    # Calculate GPA
    # ------------------------------
    # GPA Formula: GPA = TotalWeightedPoint / TotalSKS
    gpa_table["GPA"] = gpa_table["TotalWeightedPoint"] / gpa_table["TotalSKS"]
    
    # Round GPA to 2 decimal places for clean reporting
    gpa_table["GPA"] = gpa_table["GPA"].round(2)

    # Display GPA for each student
    print("\n====================")
    print("GPA per Student")
    print("====================")
    print(gpa_table[["StudentID", "Student Name", "Group", "GPA"]])

    # Display average GPA of the class (rounded to 2 decimals)
    average_gpa = gpa_table["GPA"].mean()
    print("\n====================")
    print("Average GPA (Class)")
    print("====================")
    print(f"{average_gpa:.2f}")

    # ------------------------------
    # Save Clean GPA report into same Excel file
    # ------------------------------
    output_sheet_name = "GPA_Report"
    
    # Select only the required final columns for the clean Excel report
    final_report_df = gpa_table[["StudentID", "Student Name", "Group", "GPA"]]

    # Using ExcelWriter to write a new sheet in the same workbook
    with pd.ExcelWriter(file_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        # Save clean GPA table
        final_report_df.to_excel(writer, sheet_name=output_sheet_name, index=False)

    print("\nDone! GPA_Report has been saved into academic_data.xlsx")



if __name__ == "__main__":
    # Run main when the script is executed
    main()

