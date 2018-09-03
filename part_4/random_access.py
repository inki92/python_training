import random
word = "index"
high = len(word)
low = -len(word)
print(high)
print(low)
for i in range(10):
	position = random.randrange(low, high)
	print(word[position])
