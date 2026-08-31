import re

pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

text = """
Student Name: Atharva Parande
Department: SOC CSE - SY11
Enrollment No.: ADT25SOCB0281
Email: atharvaparandeytl@gmail.com
Contact No.: 7709006858

Other emails:
support@example.com
student.help@college.co.in
"""

emails = re.findall(pattern, text)

print("Emails found:")
for email in emails:
    print(email)

email = input("\nEnter an email to validate: ")

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")