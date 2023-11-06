#learning how to use a lambda function
# say_hello = lambda: print("Hello World!")
# say_hello()


#using lamda to double a number
# double_num = lambda num: num*2
# print(f'the double of 10 is:{double_num(10)}')

#you can also map labda into another function
original_list = [1,2,3,4,5]
new_list = list(map(lambda x:x+2, original_list))
print(new_list)