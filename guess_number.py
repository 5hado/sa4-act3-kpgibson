print("I'm thinking of a number...")
while(True):
    number = 10
    guess = int(input("What number am I thinking of? "))
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Wrong guess again.")
        if guess < number:
            print("too low")
        else:
            print("too high")