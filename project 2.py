import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_free_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def user_move(board):
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(pos, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number from 1 to 9.")

def computer_move(board):
    free = get_free_positions(board)
    if free:
        row, col = random.choice(free)
        board[row][col] = "O"

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    for turn in range(9):
        if turn % 2 == 0:
            user_move(board)
        else:
            computer_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            return
        if check_winner(board, "O"):
            print("Computer wins!")
            return
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
    