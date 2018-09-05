#this is debug version of program. If you need run this program in game-mode, please comment print-strings in cycle "while word:"
#import random module and variables
import random
#cortege with variants of words
WORDS = ("god","sun","word","world","basic","night","python","book")
#variable word - this is random choice from WORDS
word = random.choice(WORDS)
jumble = ""
min_pos = ""
max_pos = ""
correct = word
points = 100
help_pos = 0
trying = 1
while word:
#	print("orig_word = ", word)
#Choise random position from word	
	position = random.randrange(len(word))
#	print("position = ", position)
#Jumble - is letter from word(see previos comment)
	jumble += word[position]
#min_pos - is srez from word from start at jumble-letter, without jumble-letter
	min_pos = word[:position]
#max_pos - is srez from word from jumble_letter(without jumble-letter) ar end of word
	max_pos = word[(position+1):]
#this word - is new word, withoust juble_letter
	word = min_pos + max_pos
#	print("1 chapter = ", min_pos)
#	print("2 chapter = ", max_pos)
#	print("jumble = ", jumble)
#	print("final_word = ", word, "\n")
print("Hello. \nCan you guess this word?:\n", jumble)
#this variable enter a users input
print("You have 100 points for guess this word. One try = -5 points. Good luck!")
guess = input("Enter your variant of word:\n")
if guess != correct:
	print("This is incorrect version((")
#cycle with guess == correct, and guess == string
while guess != correct and correct != "":
	guess = input("Enter your variant of word, or enter 'help' for help(this is -10 points):\n")
	points -= 5
	trying += 1
	if guess == "help":
		points -= 10
		print((help_pos+1), "'s letter of this word is: ", correct[:(help_pos+1)])
		help_pos += 1
	else:
		print("This is incorrect version((")		
if guess == correct:
	if points > 0:
		print("You are winner!!!\n You have ", points, "points")
	else:
		print("You guess this word. But your points is ", points, "May be try it again?")

