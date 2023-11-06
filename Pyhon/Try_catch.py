# To illustrate the use of try_catch in Python 
# Is used to test for errors and instead of throwing an error it displays what you want it to display
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Ivalid Entry! ")
   
try:
    print(x)
except:
    print("An exception Occurred ")

try:
    print(x)
except ValueError: // You can give it an Error name i.e(ValueError)
    print("Variable x is not defined ")
except:
    print("Something else went wrong ")
    '''
try:
    num = int(input("Enter a positive integer: "))
except ValueError:
     print("Invalid Entry")
else:
      if num>0:
        print("Is a positive number")
      else:
          print("You have entered a negative number")
   
