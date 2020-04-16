# TODO: Import the random library

# Let the user have 8 chances to guess
chances = 8

# Define the range of your numbers!
upperBound = 100

# TODO: Use a function call to random.randrange() to
          # Return a random number between 0 and upperBound
answer =  

# TODO: print the sentence "Make a guess about the number!"

# TODO: print the sentence "The number is an integer between 0 and ",

# followed by the value of the upperBound


# TODO: Initialize response with the user's input


# TODO: Let guess store the integer value of response


# TODO: Print the values of answer and response to see if everything works!


# TODO: Delete the  print statements for answer and response before moving on

# Repeat until the guess is equal to answer
while False: # TODO: Replace false with the correct logic 

    # Decrease the number of remaining guesses by 1
    
    # If we don't have any guesses left
    # Tell the user they're out of chances, and show the answer

    if False: # TODO: Replace false with the correct logic
        print("Aw... You didn't manage to guess the answer")
        print("The correct number is: " + str(answer))
        
        # TODO: After printing the above statements, skip over
        # all remaining iterations

    # TODO: If guess is smaller than the answer, print something telling 
    # the user to enter a bigger number (make sure to use the value of guess)

    # TODO: else if guess is smaller than the answer, print something telling 
    # the user to enter a bigger number (make sure to use the value of guess)
    

    # Because the chances are not depleted, ask the user to
    # Enter a new guess and tell the num of chances left, updating response
    response = input("Guess again: (" + str(chances) + " chances left)")

    # Once again, update guess by parsing response into an integer
    guess = int(response)

# If the user guessed the correct answer, congratulate them and print the correct answer
