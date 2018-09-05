text = input("Enter you text:\n")
max = len(text)
all_word = ""
while max != 0:
	all_word += text[max-1]
	max -= 1
print(all_word)		
