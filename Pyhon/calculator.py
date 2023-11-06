
num1 = int(input('Enter a positive integer: '))
operator = input("Input an operator (+, *, /, %): ")
num2 = int(input('Enter a positive integer: '))

if operator == '+':
    result = num1 + num2
    print(result)
if operator == '-':
    result = num1 - num2
    print(result)
if operator == '*':
    result = num1 * num2
    print(result)
if operator == '%':
    result = num1 % num2
    print(result)
    
