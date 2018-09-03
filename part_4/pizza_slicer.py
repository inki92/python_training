pizza = "pizza"
start = None
while start != "":
	start = input("Your start position: ")
	if start:
		start = int(start)
		finish = int(input("Your finish position: "))
		print(pizza[start:finish])
