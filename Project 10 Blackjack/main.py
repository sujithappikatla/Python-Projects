
import random
from replit import clear
from art import logo

user_cards = []
computer_cards = []

def deal_card():
  """ Randomly choose one card"""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def user_card_sum(for_print="no"):
  if 11 in user_cards and sum(user_cards)==21 and len(user_cards)==2 and for_print=="no":
    return 0
  return sum(user_cards)

def computer_card_sum(for_print="no"):
  if 11 in computer_cards and sum(computer_cards)==21 and len(user_cards)==2 and for_print=="no":
    return 0
  return sum(computer_cards)

def cards_print():
  print(f"Your cards : {user_cards} , current score : {user_card_sum('yes')}")
  print(f"Computer's first card : {computer_cards[0]}")

def is_game_over():
  game_over = False;
  if computer_card_sum()>21 or user_card_sum()>21:
    if 11 in computer_cards :
      computer_cards.remove(11)
      computer_cards.append(1)
    if 11 in user_cards :
      user_cards.remove(11)
      user_cards.append(1)

  if user_card_sum()==0 or computer_card_sum()>21:
    print("You Won!!")
    game_over = True
  elif computer_card_sum()==0 or user_card_sum()>21:
    print("You lose.... ")
    game_over = True
  if game_over:
    print(f"Your end Score : {user_card_sum('yes')} , Computer end score : {computer_card_sum('yes')} ")   
  return game_over

def select_winner():
  if user_card_sum() > computer_card_sum():
    print("You Won!!")
  else:
    print("You Lose...")
  print(f"Your end Score : {user_card_sum('yes')} , Computer end score : {computer_card_sum('yes')} ")
  print("*************************************************")

new_game = "y"
while new_game == "y":
  clear()
  print(logo)
  user_cards = []
  computer_cards = [];
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  cards_print()
  gameover = is_game_over()
  if not gameover:
    user_will_draw = input("Type 'y' to get another card, type 'n' to pass : ")
    while user_will_draw=="y" and not gameover:
      user_cards.append(deal_card())
      cards_print()
      gameover = is_game_over()
      if not gameover:
        user_will_draw = input("Type 'y' to get another card, type 'n' to pass : ")

    while computer_card_sum() < 17 and not gameover:
      computer_cards.append(deal_card())
      gameover = is_game_over()
    
  if not gameover:
    select_winner()
  new_game = input("Do you want to play new game of Blackjack? Type 'y' or 'n' : ")
