import random
tries = 0
number = ""
eagle = 0
back = 0
while tries != 100:
	number = random.randrange(2)
	tries += 1
	if number == 0:
		back += 1
	elif number == 1:
		eagle += 1
	else:
		print("Error")
print("Back = ", back, "\nEagle = ", eagle)
