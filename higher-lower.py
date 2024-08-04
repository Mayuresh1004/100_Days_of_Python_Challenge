#To Do 1: Print Higher lower logo
from art import logo
from art import vs
from game_data import data
import random
from replit import clear
should_continue=True
score=0

print(logo)
#To Do 2: Import the data of 2 compititors using dict
acc_A=0
acc_B=0
def player_A():
  global acc_A
  acc_A=random.randint(0,len(data)-1)
  return f"{data[acc_A]['name']} , a {data[acc_A]['description']} , from {data[acc_A]['country']}"

def player_B():
  global acc_B
  acc_B=random.randint(0,len(data)-1)
  return f"{data[acc_B]['name']} , a {data[acc_B]['description']} , from {data[acc_B]['country']}"



def compare():
  global should_continue
  global score
  ask=input("Who has more followers? Type 'A' or 'B'.").lower()
  
  if ask=="a":
    if data[acc_A]['follower_count']>data[acc_B]['follower_count']:
      clear()
      print(logo)
      score+=1
      print(f"You're right. current score={score}")
    else:
      clear()
      print(f"Sorry, thats wrong. Final score: {score}")
      should_continue=False
      
      
  elif ask=="b":
    if data[acc_B]['follower_count']>data[acc_A]['follower_count']:
      clear()
      print(logo)
      score+=1
      print(f"You're right. current score={score}")
    else:
      clear()
      print(f"Sorry, thats wrong. Final score: {score}")
      should_continue=False
      


Player_A=player_A()
Player_B=player_B()
#To Do 5: Compare B with another randomly until player looses
while should_continue==True:

  if Player_A!=Player_B:
    print(data[acc_A]['follower_count'])
    print(data[acc_B]['follower_count'])
    print(f"Compare A :{Player_A}")
    print(vs)
    print(f"Compare B :{Player_B}")
  
    compare()
    
    Player_A=Player_B
    data[acc_A]['follower_count']=data[acc_B]['follower_count']
    Player_B=player_B()
  else:
    Player_A=player_A()
    Player_B=player_B()
    if Player_A!=Player_B:
      print(data[acc_A]['follower_count'])
      print(data[acc_B]['follower_count'])
      print(f"Compare A :{Player_A}")
      print(vs)
      print(f"Compare B :{Player_B}")

      compare()

      Player_A=Player_B
      data[acc_A]['follower_count']=data[acc_B]['follower_count']
      Player_B=player_B()
#To Do 6: Display final score if the user looses