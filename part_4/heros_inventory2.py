inventory = ("sword",
		"arm",
		"magic")
print("In your arsenal:\n")
for item in inventory:
	print(item)
print("In your arsenal", len(inventory), "items")
inv = input("Enter number\n")
if inv in inventory:
	print("you have ",inv)
index = int(input("Enter index\n"))
print("This is", inventory[index])
start = int(input("Enter start position\n"))
finish = int(input("Enter finish position\n"))
print("This is", inventory[start:finish])
chest = ("Gold", "Silver")
print(chest)
inventory += chest
print(inventory)
