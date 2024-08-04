from art import logo
import random

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")

number=random.randint(1,100)


def easy_level():
  attempts=10
  
  while attempts > 0:

    print(f"You have {attempts} attempts left.")
    guess=int(input("Make a guess: "))
     
    if guess > number:
      print("Too high.")
      attempts-=1
      if attempts!=0:
        print("Guess again")
      else:
        print("You've run out of guesses, you lose.\n")
        print(f"The number was {number}")
        
    elif guess < number:
      print("Too low.")
      attempts-=1
      if attempts!=0:
        print("Guess again")
      else:
        print("You've run out of guesses, you lose.\n")
        print(f"The number was {number}")
    else:
      print(f"You got it! The answer was {number}.")
      attempts=0
      break
  
  

def hard_level():
  attempts=5
  while attempts > 0:

    print(f"You have {attempts} attempts left.")
    guess=int(input("Make a guess: "))

    if guess > number:
      print("Too high.")
      attempts-=1
      if attempts!=0:
        print("Guess again")
      else:
        print("You've run out of guesses, you lose.\n")
        print(f"The number was {number}")
    elif guess < number:
      print("Too low.")
      attempts-=1
      if attempts!=0:
        print("Guess again")
      else:
        print("You've run out of guesses, you lose.\n")
        print(f"The number was {number}")
    else:
      print(f"You got it! The answer was {number}.")
      attempts=0
     


difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty=="easy":
  easy_level()

elif difficulty=="hard":
  hard_level()

else :
  print("Plaese Enter a Valid Input!")
