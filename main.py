from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1,50)

user_choice = int(input("Choose your number : "))

playing = True
while playing:
  if user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher")
