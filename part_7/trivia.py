import sys
def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode, encoding = 'utf-8')
    except IOErrod as e:
        print("Can't open file")
        sys.exit()
    else:
        return the_file
def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        correct = next_line(the_file)
        if correct:
            correct = correct[0]
            explanation = next_line(the_file)
    return category, question, answers, correct, explanation
def welcome(title):
    print("Hello")
    print("\t\t", title, "\n")
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        print(category)
        print  (question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        answer = input("Your variant: ")
        if answer == correct:
            print("\nYes!", end = " ")
            score += 1
        else:
            print("\nNo.", end = " ")
        print(explanation)
        print("Score: ", score, "\n\n")
        category, question, answers, correct, explanation = next_block(trivia_file)
        trivia_file.close()
        print("This is last question. Your score is ", score)
main()
