def parse_preview(preview):
    """
    Converts a preview string into a nested list structure
    so individual letters can be updated.

    Example preview:
    "_  _  _   _ _ _"

    -> parsed as list of words containing underscores
    """
    # Split by triple space to separate words, then by double space for letters
    return [word.split("  ") for word in preview.split("   ")]


def update_preview(parsed, pos, new_letter):
    """
    Replaces the underscore at a specific global index (pos)
    with a new letter inside the parsed preview structure.

    Word/letter indexing currently depends on fixed character layout.
    This part can be made dynamic later.
    """
    word_index = -1
    letter_index = -1

    # Position mapping logic (specific to your final puzzle layout)
    if pos < 5:
        word_index, letter_index = 0, pos

    elif 5 < pos < 11:
        word_index, letter_index = 1, pos - 6

    elif 11 < pos < 14:
        word_index, letter_index = 2, pos - 12

    elif 14 < pos < 19:
        word_index, letter_index = 3, pos - 15

    else:
        return parsed

    parsed[word_index][letter_index] = new_letter.upper()
    return parsed


def build_preview(parsed):
    """ Rebuild preview string from nested list structure. """
    return "   ".join("  ".join(word) for word in parsed)


def check_answer(user_input, answer, preview):
    """
    Compares user input letter-by-letter to the final answer.
    Reveals letters in preview only if they match in the correct position.
    """
    for pos, char in enumerate(user_input):
        if pos < len(answer) and char == answer[pos] and char != " ":
            parsed = parse_preview(preview)
            parsed = update_preview(parsed, pos, char)
            preview = build_preview(parsed)

    return preview
