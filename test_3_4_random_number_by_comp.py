import random

max_numb = int(input("Enter max number\n"))
users = ""
middle = max_numb // 2
numb = middle
while users != "<":
	if users == "yes":
		break
	else:			
		print("This is = ", numb, "Plaese say '<', '>' or 'yes'")
		users = input()
		numb = random.randint(1, middle)
		middle = numb
while users != ">":
	if users == "yes":
		break
	else:
		print("This is = ", numb, "Plaese say '<', '>' or 'yes'")
		users = input()
		numb = random.randint(middle, max_numb)
		middle = numb
print("!!!!")

		
		
	
	
