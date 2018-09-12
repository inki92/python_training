def display(message):
    """print message"""
    print(message)
def give_me_five():
    five = 5
    return five
def ask_yes_no(question):
    """question with yes-no answer"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

display("this function display\n")
number = give_me_five()
print("Response by function give_me_five", number)
answer = ask_yes_no("Enter y or n \n")
print("Your answer is", answer)
