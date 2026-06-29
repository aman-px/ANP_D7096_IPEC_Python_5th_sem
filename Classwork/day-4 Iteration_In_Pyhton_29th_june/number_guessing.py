# Number Guessing Game

secret_number = 37

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("Correct Guess!")
        break