import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")
print(df[["Name", "Department", "Salary"]])

avg = df.groupby("Department")["Salary"].mean()
print(avg)

avg.plot(kind="bar")
plt.ylabel("Average Salary")
plt.show()