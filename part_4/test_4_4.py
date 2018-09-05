import random
WORDS = ("sun", "man")
word = random.choice(WORDS)
trying = 0
jumble = ""
letter = ""
print("Can you guess the word? You have 5 tryes.")
while trying <= 5:
	letter = input("Enter your letter, or inter all word, if you can:\n")
	trying += 1
	if letter in word:
		print("Yes! This letter is in word.")
	else:
		print("No. This letter isn't in word")
if letter == word:
	jumble == word
else:
	jumble = input("Now you must trying enter all word:\n")
if jumble == word:
	print("Yes! You are winner!")
else:
	print("No. Try it again?")
