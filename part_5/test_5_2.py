items = {"ARM":0, "SWORD":0, "SPY":0}
print("""
        1 - edit points
        0 - exit
        """
        )
summ = items.get("ARM") + items.get("SWORD") + items.get("SPY")
summ_2 = 0
choise = None
while choise != "0":
    for i in items:
        print(i, "\t", items[i])
    summ = items.get("ARM") + items.get("SWORD") + items.get("SPY")
    print("All used points is - ", summ)
    summ_1 = 30 - summ
    print("Free points is - ", summ_1)
    choise = input("Enter your choise:\n")
    if choise == "1":
        select = input("Enter characteristic\n")
        if select in items:
            select_2 = int(input("Enter points\n"))
            summ = items.get("ARM") + items.get("SWORD") + items.get("SPY")
            summ_2 = summ + select_2
            if summ_2 > 30:
                print("\nThis too mach!!!\n")
            else:
                items[select] = select_2
print("Good buy!")
