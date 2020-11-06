# Starting at row 4 ending at 163
# A == County Name
# F == Total Trump
# K == Total Biden
# P == Total Jorgensen

# Output (to EXCEL)
# COUNTY WINNER PCT

import openpyxl

input_wb = openpyxl.load_workbook('ga_votes.xlsx')
output_wb = openpyxl.Workbook()

input_ws = input_wb["1"]
output_ws = output_wb.active

output_ws["A1"] = "County Name"
output_ws["B1"] = "Winner"
output_ws["C1"] = "Percentage"

range = input_ws["A4:P163"]
output_row_num = 1

for row in range:
    output_row_num += 1
    name = row[0].value
    trump = row[5].value
    biden = row[10].value
    jorgensen = row[15].value
    # print(f"{name:<30}{trump:10}{biden:10}{jorgensen:10}")
    total = trump + biden + jorgensen
    if trump > biden and trump > jorgensen:
        pct = trump / total
        # print(f"{name:30}{'Trump':10}{pct:>10.2f}%")
        output_ws["A" + str(output_row_num)] = name
        output_ws[f"B{output_row_num}"] = "Trump"
        output_ws[f"C{output_row_num}"] = pct
    elif biden > trump and biden > jorgensen:
        pct = (biden / total)
        output_ws["A" + str(output_row_num)] = name
        output_ws[f"B{output_row_num}"] = "Biden"
        output_ws[f"C{output_row_num}"] = pct
    else:
        pct = (jorgensen / total)
        output_ws["A" + str(output_row_num)] = name
        output_ws[f"B{output_row_num}"] = "Jorgensen"
        output_ws[f"C{output_row_num}"] = pct

output_wb.save('ga_votes_summary.xlsx')
