import random
number = random.randint(1, 100)
print("Enter number 1-100\n")
tries = 1
usernumb = ""
while usernumb != number:
	usernumb = int(input())
	tries += 1
	if usernumb > number:
		print("Your number >")
	else:
		print("Your number <")
print("Congratiluations!!!", number, "tries =", tries)

