import csv

with open('TD.csv') as csvfile:
    reader =csv.reader(csvfile)
    for row in reader:
        print(row[0], row[1],sep="|")