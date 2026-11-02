import gc

print("Name: Atharva Parande")
print("Garbage collection enabled:", gc.isenabled())

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
print("Object created:", s1.name)

del s1
print("Object reference deleted.")

collected = gc.collect()

print("Garbage collection completed.")
print("Objects collected:", collected)

gc.disable()
print("Garbage collection disabled:", gc.isenabled())

gc.enable()
print("Garbage collection enabled:", gc.isenabled())
