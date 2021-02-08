from replit import clear
from art import logo
print(logo)

any_more_bidders = True;
bidders = {}

def calculate_bid_won():
  bidder_won = ""
  bid_won = -1
  for bidder in bidders:
    if bidders[bidder] > bid_won :
      bid_won = bidders[bidder]
      bidder_won = bidder
  print(f"Winner is {bidder_won} with a bid of {bid_won}")

while any_more_bidders:
  name = input("What is your name? : ")
  bid = int(input("what is your bid? : "))
  bidders[name] = bid
  choice = input("Are there any more bidders? Type 'yes' or 'no' : ")
  clear()
  if choice=="yes":
    any_more_bidders = True
  else:
    any_more_bidders = False
    calculate_bid_won()

