from modules.utils import build_number_hint_line
from config import print_question, print_letters
from modules.final_phrase import check_answer
from modules.utils import load_questions, load_letters_mapping

def play_question(q, letters_mapping, collected_letters):
    """
    Handles one question interaction:
    - Prints question
    - Gets user input
    - If user fails, show number hints
    - On success, store letter-number pairs
    """
    answered = False
    help = False

    while not answered:

        # Build number hint list for the answer letters
        numbers = [(ch, str(letters_mapping.get(ch, '?'))) for ch in q['answer'].upper()]

        print("\n" + "= " * 50)
        
        # Display collected letters so far
        print_letters(collected_letters)

        # Show question and possibly hints
        print_question(q, numbers, collected_letters, help)
        
        user_input = input("> ").strip().upper()

        if user_input != q['answer'].upper():
            # Wrong answer → enable hints next loop
            help = True
        else:
            print("Correct!")

            # Add new discovered letters to the collection
            for ch in q['answer'].upper():
                number = letters_mapping.get(ch, '?')
                # Only add if letter not already discovered
                if not any(ch == c for c, n in collected_letters):
                    collected_letters.append((ch, number))

            answered = True

def play_riddle(question, letters_mapping, collected_letters):
    """
    Final puzzle stage:
    - Shows preview with blanks
    - Displays letter→number mappings beneath
    - Gradually reveals correct letters when user guesses
    """
    preview = "_  _  _  _  _   _  _  _  _  _   _  _   _  _  _  _"
    numbers = [(ch, str(letters_mapping.get(ch, '?'))) for ch in question['answer'].upper()]
    answered = False

    while not answered:
        if "_" not in preview:
            print("\nCorrect! The full message is:")
            print(question['answer'])
            return

        print("\n================= FINAL RIDDLE =================")
        print(question["question"])
        print("\n ", preview)
        print(build_number_hint_line(numbers, collected_letters))

        user_input = input("> ").strip().upper()
        preview = check_answer(user_input, question['answer'].upper(), preview)

def play_game():
    """
    The main game loop:
    - Loads questions + letter-to-number mapping
    - Sequentially plays the 10 mini questions
    - Unlocks and runs the final riddle
    """
    questions = load_questions()
    letters_mapping = load_letters_mapping()

    collected_letters = []  # stores discovered (letter, number) pairs

    # Play the first 10 questions
    for q in questions:
        if q['id'] >= 11:   # stop before the final puzzle
            break
        play_question(q, letters_mapping, collected_letters)

    # Final Section
    print("\n" + "= " * 50)
    print("\n" + "= " * 50)
    print("Collected letters:", collected_letters)

    # The 11th item is assumed to be the final riddle
    play_riddle(questions[10], letters_mapping, collected_letters)