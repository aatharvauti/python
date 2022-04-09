# Write a Python program to read each row from a given csv file and print a list of strings.

import csv

with open('sample.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in data:
        print(', '.join(row))