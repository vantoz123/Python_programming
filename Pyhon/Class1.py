# a guessing game

secret_number = 9
guess = ""
guess_limit = 3
count = 0
out_of_guesses = False

while secret_number != guess and not out_of_guesses:
    if count < guess_limit:
        print("Enter your guess: ")
        count += 1
        
    else:
        print("You win! ")
        
if out_of_guesses == True:
    print("You are out of guesses, YOU LOOSE! ")
else:
    print("You win! ")