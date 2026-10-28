import csv

total = {}

with open("attendance.csv", "r") as f:
    for row in csv.DictReader(f):
        name = row["Name"]
        total[name] = total.get(name, 0) + int(row["Attendance"])

for name, attendance in total.items():
    print(name, attendance)