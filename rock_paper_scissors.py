import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if wins[player] == computer:
        return "player"
    return "computer"

def play():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        if player_choice not in ("rock", "paper", "scissors"):
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    play()
