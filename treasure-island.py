print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at a crossroads. To the left is a dark forest, to the right is a lake")
direction = input("Which way do you want to go? Left or Right?\n")
direction = direction.lower()
if direction == "left":
          print("You walk into the forest and are attacked by a bear.\n")
          decision=input("Will you fight or run?\n")
          decision=decision.lower()
          if decision == "fight":
                    print("You're brave, but the bear is too strong. Game over.\n")
          elif decision == "run":
                    print("You find a portal and get teleported to the treasure island.\n")
                    print("You Enter the Treasure Island and went in a cave\n")
                    print("In That Cave there are 3 doors Which one will you choose?\n")
                    door=input("Which door will you choose? Red, Blue or Yellow?\n")
                    door=door.lower()
                    if door == "red":
                              print("You entered the room and a dragon burned you alive. Game over.")
                    elif door== "blue":
                              print("You entered the room and you found the treasure. You win!Congratulations!")
                    elif door == "yelllow":
                              print("You entered the room and a monster ate you alive. Game over.")
                    else:
                              print("Please enter a valid input")
          else:
                    print("Please enter a valid input")
elif direction=="right":
          print("You entered the lake and you spotted by a shark.\n")
          decision=input("Will you fight or run?\n")
          decision=decision.lower()
          if decision == "fight":
                    print("You're brave, but the shark is too strong. Game over.\n")
          elif decision == "run":
                    print("You run away and find a merchant who offers you a ride to the treasure island.\n")
                    print("You Enter the Treasure Island and went in a cave\n")
                    print("In That Cave there are 3 doors Which one will you choose?\n")
                    door=input("Which door will you choose? Red, Blue or Yellow?\n")
                    door=door.lower()
                    if door == "red":
                              print("You entered the room and a dragon burned you alive. Game over.")
                    elif door == "blue":
                              print("You entered the room and you found the treasure. You win!Congratulations!")
                    elif door == "Yellow":
                              print("You entered the room and a monster ate you alive. Game over.")
                    else:
                              print("Please enter a valid input")
          else:
                    print("Please enter a valid input")
else:
          print("Please enter a valid input.")