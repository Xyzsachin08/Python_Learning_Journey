import csv
with open("xyz.csv","a") as file:
    data = csv.writer(file)
    data.writerow(["sachin",9.09,"Pune"])