# Exercise 1: Calculate salary (if statements)

name = input("Enter name: ")
rate = float(input("Enter rate (two decimal places): $"))
hours = float(input("Enter hours (two decimal places): "))

rate = round(rate, 2)
hours = round(hours, 2)

net = round(rate * hours, 2)

if rate > 45.0:
    tax = net * 0.002
else:
    tax = net * 0.001

print("Tax: $", round(tax, 2)) 
salary = net - tax 
print("Salary after tax: $", round(salary, 2))


# Exercise 2: Calculate grade from marks 

subject = input("Enter subject: ")

while True:
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    
    print(f"{name}'s grade: ", end= "")

    if marks >= 80:
        print("Distinction")
    elif marks > 60:
        print("Credit")
    elif marks > 50:
        print("Pass")
    else:
        print("Fail")


    
