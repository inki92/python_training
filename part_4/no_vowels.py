message = input("Enter any message: \n")
new_message = ""
VOWELS = "eyuioa"
for letter in message:
	if letter.lower() not in VOWELS:
		new_message += letter
		print("Create new string: ", new_message)
print(new_message)
