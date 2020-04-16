import random # lets us use random functions

# Let the user have 8 chances to guess
chances = 8

# Define the range of your numbers!
upperBound = 100
answer = random.randrange(upperBound)
    
print("Make a guess about the number!")
print("The number is an integer between 0 and " + str(upperBound))

# Get the user's response and change it into an integer
response = input()
guess = int(response)

while guess != answer:
    # Decrease the number of remaining guesses by 1
    chances-=1
    # If we don't have any guesses left
    # Tell the user they're out of chances, and show the answer
    if chances == 0:
        print("Aw... You didn't manage to guess the answer")
        print("The correct number is: " + str(answer))
        break

    # If guess is smaller than the answer,
    # Tell the user to enter a larger number
    if guess < answer:
        print("The answer is greater than " + str(guess))

    # If guess is greater than the answer,
    # Tell the user to enter a smaller number
    elif guess > answer:
        print("The answer is smaller than " + str(guess))

    # Because the chances are not depleted, ask the user to
    # Enter a new guess and tell the num of chances left, updating response
    response = input("Guess again: (" + str(chances) + " chances left)")

    # Once again, update guess by parsing response into an integer
    guess = int(response)

# If the user guessed the correct answer, congratulate them!
if guess == answer:
    print("Congratulations! You guessed the correct answer")
    print("The answer is: " + str(answer))
