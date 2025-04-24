import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        # Get player's choice
        player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to end): ").lower()
        
        if player_choice == 'quit':
            break
        
        if player_choice not in choices:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue

        # Computer's choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nScore - You: {player_score}, Computer: {computer_score}")

    print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()