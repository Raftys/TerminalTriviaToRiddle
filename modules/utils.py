import json
import os


def load_json(file_name):
    """
    Loads a JSON file from the /data directory and returns it as a Python object.
    Returns None if file is missing or invalid JSON.
    """
    base_path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)

    try:
        with open(base_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print(f"ERROR: File '{file_name}' not found inside /data/")
        return None

    except json.JSONDecodeError:
        print(f"ERROR: JSON format error in '{file_name}'")
        return None


def load_questions():
    """ Load all question objects from questions.json """
    return load_json("questions.json")


def load_letters_mapping():
    """ Load letter → number mapping from letters_mapping.json """
    return load_json("letters_mapping.json")


def build_number_hint_line(numbers, collected_letters):
    """
    Builds the line of numbers that appears under the preview blanks.
    Only shows numbers for letters the player has already discovered.
    
    numbers format example: [("M","10"),("O","3"),("N","7")]
    collected_letters example: [("M",10),("N",7)]
    
    Output visually aligns based on previous number spacing.
    """
    numbers_line = ""
    prev_num = 0

    for ch, num in numbers:
        # If letter already discovered, show its number
        if any(ch == c for c, n in collected_letters):
            numbers_line += (" " if prev_num >= 10 else "  ") + num
            prev_num = int(num)

        # Preserve spacing layout
        elif ch == " ":
            numbers_line += " "
        else:
            numbers_line += "   "

    return numbers_line
