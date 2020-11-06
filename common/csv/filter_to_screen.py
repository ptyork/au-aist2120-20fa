# Text File Formats
#    TXT -- Usually this is "fixed width" data format
#    CSV -- Comma Separated Value
#    JSON -- Javascript Object Notation
#    XML -- eXtensible Markup Language
#    YAML -- YAML Ain't Markup Language

# With CSV access in ONLY sequential
# With CSV ALL values in a row are treated as STRINGS

import csv
import sys

if len(sys.argv) >= 2:
    filter_string = sys.argv[1]
else:
    filter_string = ""

with open('thousand.csv', 'rt') as csv_file:
    csv_reader = csv.reader(csv_file)

    rownum = 0
    for row in csv_reader:
        rownum += 1

        if rownum == 1:
            # print(row)
            print(f"{row[0]:<30}{row[1]:<30}{row[13]:>15}")
        else:
            region = row[0]
            if region.startswith(filter_string):
                # print(row)
                print(f"{row[0]:<30}{row[1]:<30}{row[13]:>15}")
