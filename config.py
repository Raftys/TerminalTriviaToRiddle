from modules.utils import build_number_hint_line

def welcome_message():
    print("====================================")
    print("     Welcome to the Co-op Puzzle Game")
    print("====================================\n")
    print("You will answer 10 questions.")
    print("Each correct answer reveals new letters & numbers.")
    print("At the end, use them to solve the final hidden phrase!\n")
    input("Press Enter to start the game...")


def print_question(q, numbers, collected_letters, help):
    """
    Prints the question and preview blanks.
    If help=True, also prints the number hints underneath.
    """

    # Display question with its blanks
    question_header = f"\nQuestion {q['id']}: {q['question']} "
    print(question_header + q['preview'])

    # Only display help numbers if requested
    if help:
        number_line = build_number_hint_line(numbers, collected_letters)
        # Align numbers directly under the blanks visually
        print(" " * (len(question_header) - 3) + number_line)


def print_letters(collected_letters):
    """
    Display collected letters in alphabetical order.
    Example: A - 2, C - 5, T - 7
    """
    for ch, num in sorted(collected_letters, key=lambda x: x[0]):
        print(f"{ch} - {num}", end=", ")
    print()  # New line after listing