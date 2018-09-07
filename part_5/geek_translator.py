geek = {"404":"No entry", "Googling":"Search info in google.com"}
choise = None
while choise != "0":
    print("""
    0 - exit
    1 - search
    2 - add
    3 - edit
    4 - del
    5 - list
    """
    )
    choise = input()
    if choise == "0":
        print("Good bue!")
    elif choise == "1":
        term = input("Enter term:\n")
        if term in geek:
            definition = geek[term]
            print(term, "is", definition)
    elif choise == "2":
        term = input("Enter new term")
        if term not in geek:
            definition = input("Enter definition for this term")
            geek[term] = definition
        else:
            print("Error. This term is in dictionary")
    elif choise == "3":
        term = input("What term edit?")
        if term in geek:
            definition = input("Enter value")
            geek[term] = definition
        else:
            print("We have not this term in dictionary")
    elif choise == "4":
        term = input("Whats term del?")
        if term in geek:
            del geek[term]
        else:
            print("We have not this term")
    elif choise == "5":
        print(geek)
    else:
        print("Error")
