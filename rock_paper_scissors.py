import random

def get_computer_choice():
    """Return a random choice of rock, paper, or scissors."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    """Determine the winner of a round.

    Args:
        player: The player's choice ('rock', 'paper', or 'scissors').
        computer: The computer's choice ('rock', 'paper', or 'scissors').

    Returns:
        'tie' if both choices are equal, 'player' if the player wins,
        or 'computer' if the computer wins. Returns None for invalid input.
    """
    if player == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    beaten = wins.get(player)
    if beaten is None:
        return None
    if beaten == computer:
        return "player"
    return "computer"

def play():
    """Run the Rock, Paper, Scissors game loop."""
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
