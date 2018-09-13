#program prognose randome number
import random
max_numb = int(input("Enter max number for a game:\n"))
number = random.randint(1, max_numb)
tries = 1
max_tries = int(input("Max tries - "))
def ask_number():
	usernumb = ""
	while usernumb != number:
		global tries
		print("Enter your number 1 - ", max_numb, ".Trie: ", tries, "\n")
		usernumb = int(input())
		tries += 1
		if tries != max_tries:
			if usernumb > number:
				print("Number is bigger")
			else:
				print("Number is smaller")
		else:
			break
def congr():
	if tries != max_tries:
		print("Congritulations!!!")
	else:
		print("You are looser")
def main():
	ask_number()
	congr()
main()
