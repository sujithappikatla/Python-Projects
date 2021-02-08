from art import logo
import random
from replit import clear

continue_playing="y"
while continue_playing=="y":
  clear()
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of number between 1 and 100.")
  number = random.randint(1,100)
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
  if difficulty=="hard":
    attempts_left=5
  else:
    attempts_left = 10
  print(f"You have {attempts_left} attempts to guess the number.")
  while attempts_left > 0:
    guess = int(input("Make a guess : "))
    attempts_left -= 1
    if guess > number :
      print("Too High..")
    elif guess==number:
      print("You Guessed right!!!")
      attempts_left=-1
    else:
      print("Too Low..")
    if attempts_left>0 : 
      print("Guess Again")
      print(f"you have {attempts_left} attempts remaining to guess the number")

  if attempts_left==0:
    print(f"You Lost.. Correct Number id {number}")
  
  continue_playing  = input("Do You want to try again? Type 'y' or 'n' : ")
