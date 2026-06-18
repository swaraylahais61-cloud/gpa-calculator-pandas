"""README.md

Project: Academic GPA Processor (pandas + openpyxl)

Goal:
Read an Excel workbook academic_data.xlsx, calculate GPA for each student, show results, and save them back into the workbook.

Expected Excel file:
- academic_data.xlsx

Sheets and columns:
1) Subjects
   - Code
   - Subject Name
   - SKS

2) Students
   - StudentID
   - Student Name
   - Group

3) RawScores
   - ID
   - SubjectCode
   - StudentID
   - Score

Grade rules:
- A : 85-100
- B : 70-84
- C : 60-69
- D : 50-59
- E : below 50

Points rules:
- A = 4
- B = 3
- C = 2
- D = 1
- E = 0

GPA rules:
- WeightedPoint = Point * SKS
- GPA = Total WeightedPoint / Total SKS

Folder structure:
project/
├── main.py
├── grade_utils.py
├── excel_handler.py
├── requirements.txt
├── README.md
└── academic_data.xlsx

Files explanation:
1) main.py
   - Entry point.
   - Reads the three sheets.
   - Prints each DataFrame.
   - Merges RawScores with Students, then merges with Subjects.
   - Converts Score -> LetterGrade -> Point.
   - Calculates WeightedPoint.
   - Calculates GPA for each student.
   - Prints GPA per student and class average GPA.
   - Writes the GPA results into a new Excel sheet called GPA_Report in the same file.

2) excel_handler.py
   - Contains read_academic_excel(file_path)
   - Reads Subjects, Students, and RawScores into pandas DataFrames.

3) grade_utils.py
   - Contains grade conversion helper functions:
     - convert_score_to_letter_grade(score)
     - convert_letter_grade_to_point(letter_grade)

How to run:
1) Put academic_data.xlsx in the same folder as this code.
2) Install dependencies:
   pip install -r requirements.txt
3) Run:
   python main.py

Output:
- Console prints:
  - Subjects dataframe
  - Students dataframe
  - RawScores dataframe
  - GPA per student
  - Average GPA of the class
- The Excel file will be updated with a new sheet:
  - GPA_Report
"""

