#try/except
try:
    num = float(input("Insert number: "))
except:
    print("This is no number!")
try:
    num = float(input("Insert number: "))
except ValueError:
    print("This is no number2!")
for value in (None, "Hello!"):
    try:
        print("value --> float")
        print(float(value))
    except (TypeError, ValueError):
        print("This is no number")
try:
    num = float(input("\nEnter the number"))
except ValueError as e:
    print("this is no number")
    print(e)
try:
        num = float(input("Insert number: "))
except ValueError:
    print("This is no number3!")
else:
    print("Your number, ", num)
