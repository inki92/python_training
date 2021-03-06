X = "X"
O = "O"
EMPTY = " "
TIE = "Tie!"
NUM_SQUARES = 9
def display_instruct():
    print("""Hello.
            It's tic-tac-toe game.
            For make a move enter number from 0 to 8, like this:
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8
            Now we are starting!
            """)
#
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
#
def ask_number(question, low, high, step):
    """enter number from list"""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response
#
def pieces():
    go_first = ask_yes_no("Do you need first move? Enter 'y' or 'n' ")
    if go_first == "y":
        print("\nYou is X")
        human = X
        computer = O
    else:
        print("\nYou is O")
        human = O
        computer = X
    return computer, human
#
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
#
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
#
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
#
def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (2, 4, 6),
                    (0, 4, 8))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
        return None
#
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Your move. Enter number of the squere ", 0, NUM_SQUARES, 1)
        if move not in legal:
            print("Nope! You can't this!")
    print("Ok")
    return move
#
def computer_move(board, computer, human):
    board = board[ : ]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I'm change square ", end=" ")
    for move in legal_moves(board):
        board[move] == computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] == human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
#
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
#
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("3 ", the_winner, " in line!\n")
    else:
        print("Tie!\n")
    if the_winner == computer:
        print("I'm win! You not.\n")
    elif the_winner == human:
        print("You win!\n")
    elif the_winner == TIE:
        print("Tie!")
#
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
main()
