#ROCK PAPER SCISSIORS GAME
import random
options = ["rock","paper","scissors"]
player_win = 0
computer_win = 0
tie = 0
while True:
    player_choice = input("Enter(Rock,Paper Or Scissors) or (Q to Quit): ").strip().lower()
    
  
    if player_choice== "q":
        print("GAME OVER")
        print(f"SUMMARY:  YOU WON- {player_win}, COMPUTER WON- {computer_win} AND GAME TIED- {tie}")
        break
    if player_choice not in options:
        print(" Invalid choice! Try again.\n")
        continue
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("Game Tied")
        tie+=1

    elif(
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
         print("You Won!\n")
         player_win += 1

    else:
        print("You LOSE/n")
        computer_win+=1

    
