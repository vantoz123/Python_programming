from cgi import print_arguments


marks = int(input("Enter the scored marks: "))
marks>0 and marks<=100
if marks>=85 and marks<=100:
    Grade = 'A'
    print(Grade)
elif marks>=70 and marks<85:
    Grade = 'B'
    print(Grade)
elif marks>=55 and marks<70:
    Grade = 'C'
    print(Grade)
elif marks>=40 and marks<55:
    Grade = 'D'
    print(Grade)
elif marks>=0 and marks<40:
    Grade = 'F'
    print(Grade)
else:
    print_arguments('Invalid Entry!!!')