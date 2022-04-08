# Write a Python program to read each row from a given csv file and print a list of strings.

import csv

print("Atharva Auti Roll Number 1")
with open('sample.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in data:
        print(', '.join(row))