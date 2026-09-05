# Student Data System
# Demonstrates: Variables, Data Types, Input, Output and Basic Operators

print("===== STUDENT DATA SYSTEM =====")

# Taking input from the user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
age = int(input("Enter age: "))
branch = input("Enter branch: ")
marks = float(input("Enter marks: "))

# Calculating result
if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

# Displaying student information
print("\n===== STUDENT DETAILS =====")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Age        :", age)
print("Branch     :", branch)
print("Marks      :", marks)
print("Result     :", result)

# Displaying data types
print("\n===== DATA TYPES =====")
print("Name data type      :", type(name))
print("Roll number type    :", type(roll_no))
print("Age data type       :", type(age))
print("Branch data type    :", type(branch))
print("Marks data type     :", type(marks))