"""
    A simple number guessing game where the player has 3 chances 
    to guess a random number between 1 and 20.
    """
import random

answer = random.randint(1,20)
chances = 3

print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 20. You have {chances} chances to guess it!")

while chances > 0:
    try:
        guess = int(input("guess the number between 1 and 20: "))
        # Check the guess against the answer
        if guess < answer:
            result = "Oops!  Your guess was too low." #return a hint  if the guess is low
        elif guess > answer:
            result = "Oops!  Your guess was too high." #return a hint  if the guess is high
        elif guess == answer:
            result = "Nice!  You guessed correctly!" #return a success message if the guess is correct
            print(result)
            break #exit the  loop if the guess is correct
            
        print(result)
        chances -= 1
        if chances == 0:
            print(f"Sorry, you've run out of chances.\nThe correct answer was {answer}")
        else:
            print(f"You have {chances} attempts left")
  
    except ValueError:
            print("Please enter a valid number.") #input validation for non-numeric input