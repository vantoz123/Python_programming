odd_num = []
even_num = []
constraint = int(input('enter your number: '))
#constraint = int(constraint)
for i in range (0,constraint):
    if i%2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print('the odd numbers are', odd_num)
print('the even numbers are', even_num)