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
choices_art = [rock,paper,scissors]
choices_names = ["Rock","Paper","Scissors"]

user_choice  = int(input("Enter your choice 1->Rock, 2->Paper, 3->Scissors\n"))
print(f"You chosed : {choices_names[user_choice-1]} \n{choices_art[user_choice-1]}")

computer_choice  = random.randrange(1,4)
print(f"Computer chosed : {choices_names[computer_choice-1]} \n{choices_art[computer_choice-1]}")

if user_choice<1 or user_choice >3:
  print("Select a choice 1,2,3...")
elif user_choice == computer_choice:
  print("Well tried, It's a draw..")
elif user_choice==1 and computer_choice==3:
  print("Hurray!! You won..")
elif user_choice==2 and computer_choice==1:
  print("Hurray!! You won..")
elif user_choice==3 and computer_choice==2:
  print("Hurray!! You won..")
else:
  print("Booo.. You lost...")