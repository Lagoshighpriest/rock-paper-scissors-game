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


print("Welcome to rock, paper & scissors game!!!")
import random
games_images = [rock,paper,scissors]
player_choice = int(input("Hello Player, choose a number :\n 0 for rock\n 1 for paper\n 2 for scissors\n"))
computer_choice = random.randint(0,2)
print(f"computer choose {computer_choice} : ")
print(games_images[player_choice])
if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number, you lose!")
else:
   print(games_images[player_choice])
if (player_choice == 0) and (computer_choice == 2):
  print("You win!")
elif (player_choice > computer_choice):
  print("You win!")
elif (computer_choice == 0 ) and (player_choice == 2):
  print("You lose!")
elif (computer_choice > player_choice):
  print("You lose!") 
elif (player_choice == computer_choice):
  print("It's a draw!")


  