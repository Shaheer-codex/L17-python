import random
playing = True
number = str(random.randint(0,9))

print("Guess the number between 0 and 9")
print("The game ends when you guess the number correctly")

while playing:
    guess = input("Enter your guess: ")
    if guess == number:
        print("Congratulations! You guessed it correctly")
        print("The number was: " , number)
        break
    else:
        print("Wrong guess. Try again!")