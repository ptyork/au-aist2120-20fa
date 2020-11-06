# Starting at row 4 ending at 163
# A == County Name
# F == Total Trump
# K == Total Biden
# P == Total Jorgensen

# Output
# COUNTY WINNER PCT

import openpyxl

wb = openpyxl.load_workbook('ga_votes.xlsx')

ws = wb["1"]

range = ws["A4:P163"]

for row in range:
    # print(row)
    # print(row["A"])   NOOOOO, row is a tuple
    # A == 0, F = 5, K = 10, Q = 15
    # name_cell = row[0]
    # print(name_cell.value)
    name = row[0].value
    trump = row[5].value
    biden = row[10].value
    jorgensen = row[15].value
    # print(f"{name:<30}{trump:10}{biden:10}{jorgensen:10}")
    total = trump + biden + jorgensen
    if trump > biden and trump > jorgensen:
        pct = (trump / total) * 100
        print(f"{name:30}{'Trump':10}{pct:>10.2f}%")
    elif biden > trump and biden > jorgensen:
        pct = (biden / total) * 100
        print(f"{name:30}{'Biden':10}{pct:>10.2f}%")
    else:
        pct = (jorgensen / total) * 100
        print(f"{name:30}{'Jorgensen':10}{pct:>10.2f}%")
