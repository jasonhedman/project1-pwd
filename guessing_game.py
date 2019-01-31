"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def validate(guess):
  return (guess >= 1 and guess <= 10)

def repeat(response):
  return (response.upper() == "Y")

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
   
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    
    #TODO: validate the input
    print("Welcome to the number guessing game! You will be continuously asked to guess a number until you guess correctly.")
    replay = "Y"
    high_score = 10
    while(repeat(replay)):
      if(high_score != 10):
        print("The current high score is", high_score)
      answer = random.randint(1,11)
      guess = ""
      counter = 0
      while(guess != answer):
        try:
          guess = int(input("What is your guess? "))
          if(validate(guess)):  
            if(guess > answer):
              print("It's lower")
            else:
              print("It's higher")
            counter+=1
          else:
            print("You must guess a number bewteen 1 and 10. Please try again.")
            guess = int(input("What is your guess? "))
        except ValueError:
          print("Please input a valid integer.")
      print("Got it! It took you", counter, " guess(es)")
      if(counter<high_score):
        high_score = counter
      replay = input("Would you like to play again? [Y]/[N]")
    print("The game is ending now. Your high score was", high_score)
    
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
