# import csv

# with open('testinglocations.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} TEXT {row[1]} TEXT {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

import csv
with open("testinglocations.csv", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        i = str(row[30]) #column 31
        print (i)
#        with open('testinglocations.csv', 'wb') as fx:
#        fx.write(csv)