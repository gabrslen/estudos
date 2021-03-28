import pandas as pd

n=int(input("Students "))
admno = []
name = []

for i in range (n):
    ad = input("Enter Admission no: ")
    nm = input("Enter Name: ")
    admno.append(ad)
    name.append(nm)

b = {'Admno':admno,'Name':name}
c = pd.DataFrame(b)

print(c)