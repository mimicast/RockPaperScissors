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

#Write your code below this line 👇
#rock = 0
#paper = 1
#scissor = 2

optionList = [rock, paper, scissors]

selHumanOption = int(input("Choose your destiny: "))
selOption = random.randint(0,2)

if selHumanOption == 0:
  print(optionList[selHumanOption])
elif selHumanOption == 1:
  print(optionList[selHumanOption])
elif selHumanOption == 2:
  print(optionList[selHumanOption])

if selHumanOption == 0 and selOption == 0:
  print(f"Computer chose: {optionList[selOption]}")
  print("It's a tie")
elif selHumanOption == 0 and selOption == 1:
  print(f"Computer chose: {optionList[selOption]}")
  print("You Lose")
elif selHumanOption == 0 and selOption == 2:
  print(f"Computer chose: {optionList[selOption]}")
  print("You Win")
elif selHumanOption == 1 and selOption == 0:
  print(f"Computer chose: {optionList[selOption]}")
  print("You Win")
elif selHumanOption == 1 and selOption == 1:
  print(f"Computer chose: {optionList[selOption]}")
  print("It's a tie")
elif selHumanOption == 1 and selOption == 2:
  print(f"Computer chose: {optionList[selOption]}")
  print("You Lose")
elif selHumanOption == 2 and selOption == 0:
  print(f"Computer chose: {optionList[selOption]}")
  print("You Lose")
elif selHumanOption == 2 and selOption == 1:
  print(f"Computer chose: {optionList[selOption]}")
  print("You Win")
elif selHumanOption == 2 and selOption == 2:
  print(f"Computer chose: {optionList[selOption]}")
  print("It's a tie")
else:
  print("You chose wrong \nYou lose by default")