# def sum_of_digits(n):
#     total = 0
#     while n>0:
#         total += n % 10
#         n//=10
#     return total

# num = 12345
# print(sum_of_digits(num))   

# a = input("Enter a valid integer: ")
# b = input("Enter another valid integer: ")
# try:
#     result = int(a)/int(b)
#     # print(f"The result of the division is: {result}")
# except ZeroDivisionError as e:
#     print("Invalid input! Your divisor becomes zero!")
#     print(f"Error details: {e}")
# except ValueError as e:
#     print("Invalid input! Provide a correct input next time!")
#     print(f"Error details: {e}")
# except Exception as e:
#     print("Unknown error occurred!")
#     print(f"Error details: {e}")
# else:
#     print(f"The result of the division is: {result}")
# print("The program completes successfully.")
# class MyException(Exception):
#     """ This is a custom exception."""
# try:
#     user_input = int(input("Enter an integer which is not greater than 100:"))
#     if user_input > 100:
#         raise MyException("You have made the integer greater than 100.")
#     print(f"Well done.You have entered:{user_input}")
# except MyException as e:
#     print(f"Custom exception is raised.Error Details:{e}")
# except ValueError as e:
#     print(f"Here is the error Details:{e}")

# try:
#     result = 15/0
# except ArithmeticError:
#     print("Caught the ArithmeticError.Your divisor is zero.")
# except ZeroDivisionError:
#     print("Caught ZeroDivisionError.Correct the divisor which is zero at present.")

try:
    raise BaseException('BaseException raised.')
except Exception as e:
    print(f"Error Details:{e}")