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
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type 0 for rock or 1 for paper or 2 for scissor."))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])

computer_choice = random.randint(0, 2)
print("Computer_chose:")
print(game_image[computer_choice]) 

if user_choice >= 3 and user_choice < 0:
    print("You entered a invalid a number.You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
