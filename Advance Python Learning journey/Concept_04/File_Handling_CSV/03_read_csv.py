import csv 
with open("students.csv", "r") as f:
    data = csv.reader(f, delimiter=';')
    
    
    
    for i in data:
        print(i)