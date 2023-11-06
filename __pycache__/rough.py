import random
# numcalls = 0
# def square(x):
#     global numcalls
#     numcalls = numcalls + 1
#     return (x * x)

# print(square(2))

# Seller information
'''
seller_name = " Spencer Retail"
seller_address = " 136, Garia Station Road,\n Kolkata:700084"
seller_contact = "123-456-789"
#Decorating top segment
print("-" * 50)
print(f"{seller_name}")
print(f"{seller_address}")
print("-" * 50)
apricot_price = 300
dates_price = 400
almonds_price = 500
apri_dates_combo = (apricot_price + dates_price) * .9 # 10% discount
dates_almon_combo = (dates_price + almonds_price) * .9 # 10% discount
almon_apri_combo = (almonds_price + apricot_price) * .9 # 10% discount
gift_pack = (apricot_price + dates_price + almonds_price) * .75 # 25%
print("Product(s) \tPrice (per pack)")
print(f"Apricot\t\t{apricot_price}")
print(f"Dates\t\t{dates_price}")
print(f"Almond\t\t{almonds_price}")
print(f"Combo-1\t\t{apri_dates_combo}")
print(f"Combo-2\t\t{dates_almon_combo}")
print(f"Combo-3\t\t{almon_apri_combo}")
print(f"GiftBox\t\t{gift_pack}")
# Decorating the bottom segment.
# It contains the contact information.
print("*" * 50)
print(f"For free delivery, contact {seller_contact} ")
print("*" * 50)
'''

# def roll():
#     min_value = 1
#     max_value = 6
#     roll = random.randint(min_value,max_value)
#     return roll

# value = roll()
# print(value)

# my_tuple = (1, 2, 3, 4, 5)
# print("The content of my_tuple is:")
# print(my_tuple)
# print("Reversing the tuple:")
# rev_tuple = tuple(reversed(my_tuple))
# print("The content of rev_tuple is:")
# print(rev_tuple)

# All questions
# question1 = "Q1.What is the value of the expression:2*3-4?" \
# "\n(a)1" \
# "\n(b)2" \
# "\n(c)3" \
# "\n(d)None."
# question2 = "\nQ2.What is the value of the expression:1+(2*3)/4?" \
# "\n(a)1.5" \
# "\n(b)3" \
# "\n(c)3.5" \
# "\n(d)None."
# question3 = "\nQ3.The set data type can hold duplicate values." \
# "The statement is:" \
# "\n(a)False" \
# "\n(b)True" \
# "\n(c)Partially correct." \
# "\n(d)None."
# Storing the questions with answer keys
# inside the following dictionary.
# question_bank = {question1: "b",
# question2: "c",
# question3: "a"}
# print("Welcome to the MCQ test.")
# print("="*25)
# score = 0 # initial value
# for key in question_bank:
#     print(key)
# user_input = input("Type your answer(a/b/c/d):")
# if user_input == question_bank[key]:
#     score += 1
# print(f"\nYour Score:{score} out of {len(question_bank)}")




#a simple calculator
# print("=" * 50)
# print('''This is a simple calculator.
# It supports the following operations:
# i)Addition
# ii)Subtraction
# iii)Multiplication and
# iv)Division.''')
# print("=" * 50)
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# op = input("Enter an operator(+,-,*./): ")
# if op == "+":
#     sum = num1 + num2
#     print(sum)
# elif op == "-":
#     sub = num1 - num2
#     print(sub)
# elif op == "*":
#     mult = num1 * num2
#     print(mult)
# elif op == "/":
#     mult = num1 / num2
#     print(mult)
# else:
#     print("You have entered an invalid input!!!")
#     ...
# import random
# class Dice:
#     def Roll():
#         for i in range(2):
#             result = random.randint(1, 10)
#             print(result, end = " ")
#     Roll()
# import random
# class Dice:
#     def Roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second

# dice = Dice()
# print(dice.Roll())   
