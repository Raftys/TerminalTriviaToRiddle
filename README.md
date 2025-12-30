# Co-op Puzzle Game

A fun, terminal-based cooperative puzzle game designed as a digital gift.  
Players solve small personal trivia questions to gradually reveal numbers, which are then used to decode a final hidden phrase.

This version is implemented in **Python 3** and is fully terminal-based, requiring no GUI.

---

## 🧩 Game Overview

You and your partner work together to solve 10 short, personal, or humorous questions.  
Each answer reveals letters connected to secret numbers stored in a JSON mapping.  
These numbers ultimately help you decipher a final hidden phrase.

---

## 🔥 How It Works

### 1. Questions Stage

- There are **10 short questions**, mostly one-word answers about computers and personal jokes.
- When a correct answer is typed:
  - Each letter is linked to a **number** from a secret mapping (`letters_mapping.json`).
  - Letters already discovered keep the same number; duplicates are avoided.
- If the answer is incorrect or `help` is typed:
  - The question is shown again.
  - Blanks (`_`) display the answer letters.
  - Numbers under the blanks hint at already discovered letters.

This encourages **co-op play**, where one player may know certain numbers and help the other.

---

### 2. Letter & Number Collection

- All discovered letters and their numbers are tracked in a shared collection (list of tuples).
- Displayed alphabetically for clarity:

