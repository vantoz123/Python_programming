# a program to read roll no, name and marks of three subjects and calculate the total, percentage and division.
Roll_number = int(input("Input the Roll Number of the Student: "))
Name = input("Input the Name of the Student: ")
# input("Input the Marks of Physics, Chemistry and Computer Application: ")
Physics = int(input("Enter the Marks of Physics: "))
Chemistry = int(input("Enter the Marks of Chemistry: "))
Computer_Application = int(input("Enter the Marks of Computer Application: "))
Total = Physics+Chemistry+Computer_Application
Percentage = ((Total/300)*100)
print(f"Roll Number: {Roll_number}")
print(f"Name of Student: {Name}")
print(f"Marks in Physics: {Physics}")
print(f"Marks in Chemistry: {Chemistry}")
print(f"Marks in Chemistry: {Computer_Application}")
print(f"Total Marks = {Total}")
print(f"Percentage = {Percentage}")
if Percentage > 0 and Percentage <=100:
    if Percentage >80 or Percentage <=100:
        print("First")
    elif Percentage >60 or Percentage <80:
        print("Second")
    else:
        print("Fail") 