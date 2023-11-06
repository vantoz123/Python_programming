def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        print(i)
        fact*=i
    return(fact)
print('The factorial is ', factorial(5))
print(f'The factorial is {factorial(5)}')
