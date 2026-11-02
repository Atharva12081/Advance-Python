print("Name: Atharva Parande")

try:
    number = int("10")
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Exception handling demonstration completed.")
