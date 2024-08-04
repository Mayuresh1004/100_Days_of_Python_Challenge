from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bid_again=True
bidders = {}
def add_bidders(bidder_name,bid_amount):
  bidders[bidder_name]=bid_amount

while bid_again == True:
  name=input("What is Your Name?\n")
  amount=int(input("Enter Your Bidding Amount: $"))
  add_bidders(name,amount)
  ask=input("Is there any other bidder? Type 'yes' or 'no'\n").lower()
  clear()
  if ask=="yes":
    bid_again=True
    continue
  else:
    bid_again=False
highest_bid=0
for key in bidders:
  if bidders[key]>highest_bid:
    highest_bid=bidders[key]
    winner=key
  else:
    continue
print(f"The winner is {winner} with a bid of ${highest_bid}")