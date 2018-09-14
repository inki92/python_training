import random
#constants
HANGMAN = (
"""
_________
|       |
|
|
|
|
|
|
|
================
""",
"""
_________
|       |
|       O   |
|
|
|
|
|
|
================
""",
"""
_________
|       |
|       O   |       -+-
|
|
|
|
|
|
================
""",
"""
_________
|       |
|       O   |       /-+-
|
|
|
|
|
|
================
""",
"""
_________
|       |
|       O   |       /-+-/
|
|
|
|
|
|
================
""",
"""
_________
|       |
|       O   |       /-+-/
|       |
|
|
|
|
|
================
""",
"""
_________
|       |
|       O   |       /-+-/
|       |
|       |
|       |
|      |
|      |
|
================
""",
"""
_________
|       |
|       O   |       /-+-/
|       |
|       |
|       |
|      | |
|      | |
|
================
""")
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("BALL", "DOG", "KITTEN")
word = random.choice(WORDS)
so_far = "-"*len(word)
wrong = 0
used = []
print("Hello!\n")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("Used letters:\n ", used)
    print("Your word:\n", so_far)
    guess = input("Enter letter\n")
    guess = guess.upper()
    while guess in used:
        print("This letter is used")
        guess = input("Enter letter\n")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("Yes!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]

        so_far = new
    else:
        print("Letter", guess, "was not in word")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("You are dead((\n")
else:
    print("You are winner!\n")
print("Word is - ", word)
