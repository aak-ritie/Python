#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
number=random.randint(1,101)
guess_continue=False
def operation(attempt):
    while not guess_continue:
        print(f"You have {attempt} attempts remaining to guess the number")
        guess=int(input("Make a guess"))
        print(number)
        attempt-=1
        if guess==number:
            print(f"You got it the answer was {number}")
            break
        elif guess<number:
            print("Too low")
        elif guess>number:
            print("Too High")
        elif attempt==0:
            print("You are out of guesses ")
            break      
print("Welcome to number guessing game")
print("I am thinking about the numbers between 1 and 100")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="easy":
   can_guess=10
   operation(can_guess)
elif difficulty=="hard":
   can_guess1=5
   operation(can_guess1)


    
  


