WORDS = ["one", "two", "two", "three", "ang", "tool"]
used = ""
for item in WORDS:
    if item not in used:
        used = item + used
        print(item)
