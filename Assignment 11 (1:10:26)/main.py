import numpy as np
import pandas as pd

# Student Details
# Name: Atharva Parande
# Department: SOC CSE - SY11
# Enrollment No.: ADT25SOCB0281

np.random.seed(42)

data = np.random.randint(1, 101, 10)

s = pd.Series(data)

print("Pandas Series:")
print(s)