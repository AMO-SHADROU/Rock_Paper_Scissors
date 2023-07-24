import random

print("Welcome to this game.")

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
---'    ____)____
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

my_list = [rock, paper, scissors]
user_num = int(input("Enter 0 for rock, 1 for paper or 2 for scissors.\n"))
computer_number = random.randint(0,2)

user_guess = my_list[user_num]
computer_guess = my_list[computer_number]
print(f"Your guess : {user_guess}")
print(f"Computer guess : {computer_guess}")

if user_num == computer_number:
    print("Draw")
elif user_num == 0 and computer_number == 1:
    print("lose")
elif user_num == 0 and computer_number == 2:
    print("win")
elif user_num == 1 and computer_number == 0:
    print("win")
elif user_num == 1 and computer_number == 2:
    print("lose")
elif user_num == 2 and computer_number == 0:
    print("lose")
elif user_num == 2 and computer_number == 1:
    print("win")
else:
    print("Wrong number")