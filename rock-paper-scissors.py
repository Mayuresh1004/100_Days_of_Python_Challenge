import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=[rock,paper,scissors]
print("Welcome to the Rock, Paper, Scissors game")
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
# user_choice=choice[user_choice_index]

if user_choice>=3 or user_choice<0:
    print("INVALID INPUT!")
else:
    print(choice[user_choice])
    print("Computer Chose:")
    computer=random.randint(0,2)
    computer_choice=choice[computer]
    print(computer_choice)
   
    if user_choice==0 and computer==2:
        print("YOU WIN!")
    elif user_choice==2 and computer==0:
        print("YOU LOOSE!")
    elif user_choice==0 and computer==1:
        print("YOU LOOSE!")
    elif user_choice==1 and computer==0:
        print("YOU WIN!")
    elif user_choice==1 and computer==2:
        print("YOU LOOSE!")
    elif user_choice==2 and computer==1:
        print("YOU WIN!")
    elif user_choice==2 and computer==0:
        print("YOU LOOSE!")
    else:
        print("DRAW! You both chose the same")