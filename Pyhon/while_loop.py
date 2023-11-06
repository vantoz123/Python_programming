# Using a while loop calculate the factorial of a number

def calc_factorial(num):
    factorial = 1
    i = 1
    while i<= num:
        factorial*=i
        i+=1
    return factorial
#Get user input
num = int(input("Enter a number to find factorial: "))
#calculate factorial using the function
result = calc_factorial(num)
#Display results
print(f"The factorial of {num} is {result}")
