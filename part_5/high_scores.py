scores = [1000,2000,3000]
choise = None
while choise != "0":
    print("""
    Scores
    0 - exit
    1 - list
    2 - add
    3 - del
    4 - sort
    """

    )
    choise = input("Enter your choise\n")
    print()
    if choise == "0":
        print("Good bue")
    elif choise == "1":
        print("Scores")
        for score in scores:
            print(score)
    elif choise == "2":
        score = int(input("Enter your score:\n"))
        scores.append(score)
    elif choise == "3":
        score = int(input("Enter item of deleting score\n"))
        if score in scores:
            scores.remove(score)
        else:
            print("We haven't this item - ", score)
    elif choise == "4":
        scores.sort(reverse=True)
    else:
        print("In menu have not this item - ", choise)
