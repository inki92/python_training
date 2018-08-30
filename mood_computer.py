import random
print("The weather is: \n")
mood = random.randint(1, 3)
sun = random.randrange(1)
if mood == 1:
	print("Rainny")
elif mood == 2:
	print("Sunny day")
else:
	print("Nope")

