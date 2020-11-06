'''
CALCULATE THE AVERAGE OF EACH EXAM SCORE ACROSS SECTIONS.

python calc_average.py [excel file name]

Assumes for the Excel file:
 - first column is just names of students
 - the rest of the columns contain exams (ONLY 2...challenge: how to make more flexible??)
 - first row of an exam column is its name
 - rest of the rows of an exam column contain grades

Strategy:
 - Iterate over each worksheet in the workbook.
 - For each worksheet iterate over each exam column.
 - For each exam, "remember" (and aggregate) the number of scores and the total score.
 - At the end, calculate the average by dividing the total score by the total number of scores.
'''

import openpyxl
import sys

if len(sys.argv) != 2:
    print('INVALID SYNTAX')
    print('Must supply a single file name')
    exit()

# Accept the file to open as an argument
filename = sys.argv[1]

wb = openpyxl.load_workbook(filename)

grade_counts = {}     # hold number of grades per exam
# for example: {"Exam 1": 8, "Exam 2": 8}
totals = {}           # hold the total grade per exam
# for examle: {"Exam 1": 650, "Exam 2": 600}

# Iterate over each worksheet in the workbook
for ws in wb.worksheets:
    # print(ws.title)
    # ITERATE OVER THE LAST TWO COLUMNS
    #  (CHALLENGE IS HERE...HOW TO MAKE THIS MORE FLEXIBLE TO WORK WITH MORE 
    #   THAN JUST TWO GRADES)
    for col in ws["B:C"]:
        # print(col)
        # GET THE EXAM NAME FROM THE FIRST CELL IN THE COLUMN
        exam_name = col[0].value
        # print(exam_name)
        # THE REST OF THE CELLS ARE THE GRADES, SO SLICE THE
        # COLUMN TO GET JUST THESE CELLS
        grades = col[1:]
        # print(grades)
        # CREATE A VARIABLE TO HOLD THE SUM OF ALL GRADES
        total = 0
        # ITERATE OVER THE GRADE CELLS TO AGGREGATE THE TOTAL GRADE
        for cell in grades:
            # print(cell.value)
            total = total + cell.value
        # print(total)
        # CALCULATE THE AVERAGE
        avg = total / len(grades)
        # print(avg)

        # FINALLY REMEMBER THE TOTALS FOR EACH EXAM FOR THIS WORKSHEET.
        # WE'LL NEED TO KEEP ADDING TO THIS FOR ALL SUBSEQUENT WORKSHEETS.
        # WE FIRST NEED TO DETERMINE WHETHER THE EXAM HAS ALREADY BEEN ENCOUNTERED
        # BEFORE. IF NOT, WE NEED TO ADD IT TO THE DICTIONARY. IF SO, WE NEED
        # TO ACCESS THE CURRENT VALUE SO THAT WE CAN ADD TO IT.
        if exam_name in grade_counts:
            # ADD TO THE CURRENT TOTAL
            grade_counts[exam_name] = grade_counts[exam_name] + len(grades)
            totals[exam_name] = totals[exam_name] + total
        else:
            # NEW EXAM, SO JUST STORE THE VALUE
            grade_counts[exam_name] = len(grades)
            totals[exam_name] = total
           

print("EXAM AVERAGES FOR ALL SECTIONS:")

# FINALLY, ITERATE OVER ONE OF THE DICTIONARIES TO GET A LIST OF VALID KEYS.
for name in grade_counts:
    # CALCULATE AND PRINT THE TOTAL AVERAGE FOR EACH EXAM
    final_count = grade_counts[name]
    final_total = totals[name]
    total_avg = final_total / final_count
    print(f"{name}: {total_avg}")

