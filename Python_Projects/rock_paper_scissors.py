
import random

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

your_choice = int(input("Let's play a game! \nEnter:  \n0: Rock! 1: Paper! 2: Scissors! \nShoot! "))
images = [rock, paper, scissors]
machine_choice = random.randint(0,2)

print(images[your_choice])
print("Machine Chose: ", images[machine_choice])

if your_choice >=3 or your_choice < 0:
    print("You chose an invalid number. YOU LOSE!")

elif your_choice == 0 and machine_choice == 1:
    print("You Lose!")
elif your_choice == 1 and machine_choice ==2:
    print("You Lose!")
elif your_choice == 2 and machine_choice== 0:
    print("You Lose!")

elif your_choice == 1 and machine_choice == 0:
    print("You Win!")
elif your_choice == 2 and machine_choice ==1:
    print("You Win!")
elif your_choice == 0 and machine_choice== 2:
    print("You Win!")

elif your_choice == machine_choice:
    print("It's a draw.")


