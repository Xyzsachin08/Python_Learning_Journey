import csv

total = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    
    for row in reader:
        total += int(row[1])
        count += 1

print("Average =", total / count)