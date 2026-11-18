from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    separator = "+-------+-------+-------+"
    empty_line = "|       |       |       |"
    for row in board:
        print(separator)
        print(empty_line)
        print("|   " + "   |   ".join(str(cell) for cell in row) + "   |")
        print(empty_line)
    print(separator)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        move = input("Enter your move: ")
        try:
            square = int(move)
        except ValueError:
            print("Please enter a whole number from 1 to 9.")
            continue
        if not 0 < square < 10:
            print("The number must be greater than 0 and less than 10.")
            continue
        row, column = (square - 1) // 3, (square - 1) % 3
        if board[row][column] in ('O', 'X'):
            print("That square is already occupied - choose another one.")
            continue
        board[row][column] = 'O'
        return


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ('O', 'X'):
                free.append((row, column))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game.
    lines = []
    lines.extend(board)                                              # rows
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  # columns
    lines.append([board[i][i] for i in range(3)])                    # diagonal
    lines.append([board[i][2 - i] for i in range(3)])                # anti-diagonal
    return any(all(cell == sign for cell in line) for line in lines)


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)
    if free:
        row, column = free[randrange(len(free))]
        board[row][column] = 'X'


def main():
    # Squares are numbered 1-9 row by row; the computer always starts in the middle.
    board = [[3 * row + column + 1 for column in range(3)] for row in range(3)]
    board[1][1] = 'X'

    while True:
        display_board(board)
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("The computer won!")
            break


if __name__ == "__main__":
    main()
