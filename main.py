# Import the welcome message function from the config module
from config import welcome_message

# Import the main game loop function from the puzzles module
from modules.puzzles import play_game


if __name__ == "__main__":
    # Display the welcome message and instructions
    welcome_message()

    # Start the main game loop
    play_game()
