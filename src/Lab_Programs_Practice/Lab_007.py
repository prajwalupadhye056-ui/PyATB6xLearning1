#To read CSV file

import csv

with open('TD1.csv') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row[0],row[1], sep="|")