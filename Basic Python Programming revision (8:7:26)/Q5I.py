n = int(input("Enter your marks: "))

if n >= 90 :
    print("You have been awarded O grade")
elif 80 <= n >= 89:
    print("You have been awarded A+ grade")
elif 70 <= n >= 79:
    print("You have been awarded A grade")
elif 60 <= n >= 69:
    print("You have been awarded B grade")
elif 50 <= n >= 59:
    print("You have been awarded C grade")
elif  n < 50:
    print("You have been awarded F grade")