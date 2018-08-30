health = 10
trolls = 0
damage = 1
while health != 0:
	trolls += 1
	health -= damage
	print("Killing troll, but damage = ", damage, "points")
print("Your hero kill", trolls)
print("But hi is dead")
