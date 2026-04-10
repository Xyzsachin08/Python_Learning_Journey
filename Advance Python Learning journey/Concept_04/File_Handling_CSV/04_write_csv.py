import csv
with open("sachin.csv", "w") as file:
    data = csv.writer(file,delimiter=";")
    
    data.writerow(["sachin","45","borude"])
    