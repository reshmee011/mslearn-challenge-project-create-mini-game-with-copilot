import random
# write 'hello world' to the console
print('hello world')
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.

# Define valid options and winning options
valid_options = ['rock', 'paper', 'scissors']
winning_options = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

# Define player's score
score = 0

# Define function to get player's choice
def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in valid_options:
            return choice
        else:
            print("Invalid option. Please choose again.")

# Define function to choose opponent's option
def get_opponent_choice():
    return random.choice(valid_options)

# Define function to compare options and determine winner
def get_winner(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        return 'tie'
    elif winning_options[player_choice] == opponent_choice:
        return 'win'
    else:
        return 'lose'

# Define function to display result and update score
def play_round():
    global score
    player_choice = get_player_choice()
    opponent_choice = get_opponent_choice()
    result = get_winner(player_choice, opponent_choice)
    if result == 'tie':
        print(f"You both chose {player_choice}. It's a tie!")
    elif result == 'win':
        print(f"You chose {player_choice} and the opponent chose {opponent_choice}. You win!")
        score += 1
    else:
        print(f"You chose {player_choice} and the opponent chose {opponent_choice}. You lose!")
        score -= 1

# Define function to ask player if they want to play again
def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid option. Please choose again.")

# Play the game
print("Welcome to Rock-Paper-Scissors!")
while True:
    play_round()
    print(f"Your score is {score}.")
    if not play_again():
        break
print(f"Thanks for playing! Your final score is {score}.")
