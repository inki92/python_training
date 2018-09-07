scores = []
choise = None
while choise != "0":
    print("""
            0 - to exit
            1 - list scores
            2 - add record
            """
            )
    choise = input("Enter value of menu:\n")
    print()
    if choise == "0":
        print("Good bue")
    elif choise == "1":
        for entry in scores:
            score, name = entry
            print(score, name)
    elif choise == "2":
        name = str(input("Enter name:\n"))
        score = int(input("Enter record:\n"))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("In this list have not this item", choise)
