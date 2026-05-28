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

k = 1
while k==1:
    player1 = [rock,paper,scissors]
    player2 = [rock,paper,scissors]
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice>=3 and user_choice<0:
        print("Wrong I/P you lose")
    move1 = random.choice(player1)
    move2 = player2[user_choice]

    if move1 == paper and move2 == rock:
        print(f"{move1} vs {move2}")
        print("Computer win!")
    elif move1 == rock and move2 == scissors:
        print(f"{move1} vs {move2}")
        print("Computer win!")
    elif move1 == scissors and move2 == paper:
        print(f"{move1} vs {move2}")
        print("Computer win!")
    elif move2 == paper and move1 == rock:
        print(f"{move1} vs {move2}")
        print("You win!")
    elif move2 == rock and move1 == scissors:
        print(f"{move1} vs {move2}")
        print("You win!")
    elif move2 == scissors and move1 == paper:
        print(f"{move1} vs {move2}")
        print("You win!")
    else:
        print(f"{move1} vs {move2}")
        print("draw")
    user_choice = int(input("Do you want to play again? Press 1 to continue and 0 to exit.\n"))
    if user_choice !=0 and user_choice!=1:
        print("wrong I/P you lose")
    else:
        k=user_choice

    
    