print("I'm thinking of a number...")
count = 3
while(True):
    number = 10
    guess = int(input("What number am I thinking of? "))
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Wrong guess again.")
        count = count - 1
        print("You have " + str(count) + " left")
        
        if count == 0:
            print("you lost")
            break

        if guess < number:
            print("too low")
        else:
            print("too high")
