print("I'm thinking of a number...")
count = 2
while(True):
    number = 10
    guess = int(input("What number am I thinking of? "))
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Wrong guess again.")
        print("You have " + str(guess) + " left")
        count = count - 1
        
        
        if count == -1:
            print("you lost")
            break

