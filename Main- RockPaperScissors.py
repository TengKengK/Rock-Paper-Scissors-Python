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

game_images = [rock, paper, scissors]
# Get input from user and store as int
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (choice >= 3 or choice < 0):
    print("Invalid choice! You lose!")
else:
    print(game_images[choice])

    # Random choice for the bot
    robo_choice = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[robo_choice])

    if (choice == robo_choice):
        print("Tied!")
    elif (choice == 1 and robo_choice == 0):
        print("You win!")
    elif (choice == 0 and robo_choice == 2):
        print("You win!")
    elif (choice == 2 and robo_choice == 1):
        print("You win!")
    elif (choice > robo_choice):
        print("You win!")
    else:
        print("You lose!")