def fizz_buzz(input):
    if (input%3 or input%5) == 0:
        print("fizz_buzz")
    elif input%3 == 0:
        print("fizz")
    elif input%5 == 0:
        print("buzz")
    else:
        print(input)

    return fizz_buzz
    
fizz_buzz(45)
