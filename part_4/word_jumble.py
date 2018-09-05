import random
WORDS = ("god","sun","word","world","basic","night","python","book")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position+1):]
print("Hello! This anagramma: ", jumble)
guess = input("Enter ypur variant:\n")
while guess != correct and guess != "":
	print("No")
	guess = input("Enter ypur variant:\n")
if guess == correct:
	print("Good!!!")

