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
option = [rock,paper,scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))
print(f"{option[user_choice]}\nComputer chose:\n")
computer_choice = random.choice(option)
print(computer_choice)

computer_index = option.index(computer_choice)

if user_choice == 0:
  if computer_index == 0:
    print("It's a draw!")
  elif computer_index == 1:
    print("You lost!")
  else:
    print("You win!")

if user_choice == 1:
  if computer_index == 0:
    print("You win!")
  elif computer_index == 1:
    print("It's a draw!")
  else:
    print("You lost!")

if user_choice == 2:
  if computer_index == 0:
    print("You lost!")
  elif computer_index == 1:
    print("You win!")
  else:
    print("It's a draw!")    
