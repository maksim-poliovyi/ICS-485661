import csv
import sys
print("Група 1")
filename = "students2.txt"
file = open(filename, "r")
reader = csv.reader(file, delimiter="\t")
for row in reader:
    print(row) 

print("Група 2")
filename1 = "students3.txt"
file = open(filename, "r")
reader = csv.reader(file, delimiter="\t")
for row in reader:
    print(row)