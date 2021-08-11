secret_word = input("Enter your secret word for your friends to guess. ")
secret_word = secret_word.upper()
length = len(secret_word)
print("Hint: Your secret word starts with a " + "'" + secret_word[0] + "' and ends with a " + "'" + secret_word[length-1] + "'.")
print("Your word is " + str(length) + " characters long. The Game starts now. Best of luck!")
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Take your guess: ")
        guess = guess.upper()
        guess_count = guess_count+1
        if secret_word != guess:
            print("Wrong! Try again")
        else:
            print("Congratulations! You guessed it!! You win!")
            guess_count = 3
    else:
        out_of_guess = True
        print("Sorry! You're out of guesses. The correct word was " + secret_word)




