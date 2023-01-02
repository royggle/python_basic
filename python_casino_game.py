from random import randint

print("Welcome to Python Casino")
print("This game is based on tree structure in data structures theory.")
pc_choice = randint(1,50)

count = 0
playing = True
while playing:
  user_choice = int(input("Choose your number (1, 50) : "))
  if count == 11:
    print("You lost!")
    playing = False
  elif user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher")
  count += 1
  print("count : ", count)
