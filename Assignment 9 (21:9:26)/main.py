# Assignment 9 - CSV to JSON Conversion
# Name: Atharva Parande

import csv
import json


def csv_to_json(csv_file, json_file):
    data = []

    # Read data from CSV file
    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    # Write data to JSON file
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)


# Main Program
input_file = "students.csv"
output_file = "students.json"

csv_to_json(input_file, output_file)

print("CSV file converted to JSON successfully.")
print("JSON data written to:", output_file)