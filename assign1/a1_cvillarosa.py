"""
Tic Tac Toe using MinMax algorithm

This python project makes use of the MinMax algorithm.
Try it out and see if you defeat the computer. 🤖

Author: Carl Villarosa
cvillarosa2022@fau.edu
09/18/2023
"""

import random


# Create the tic-tac-toe board
def init_board():
    return [" " for _ in range(9)]

# Display the Tic-Tac-Toe board
def display_board(board):
    print("-------------")
    print(f"| {board[0] if board[0] != ' ' else '1'} | {board[1] if board[1] != ' ' else '2'} | {board[2] if board[2] != ' ' else '3'} |")
    print("-------------")
    print(f"| {board[3] if board[3] != ' ' else '4'} | {board[4] if board[4] != ' ' else '5'} | {board[5] if board[5] != ' ' else '6'} |")
    print("-------------")
    print(f"| {board[6] if board[6] != ' ' else '7'} | {board[7] if board[7] != ' ' else '8'} | {board[8] if board[8] != ' ' else '9'} |")
    print("-------------")

# Check if the board is full
def is_full(board):
    return " " not in board

# Check if the game is over whether it's win or draw
def game_over(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
        return board[4]
    
    # Check for a draw
    if is_full(board):
        return "Game is a draw!"
    
    return None

# Get available moves
def available_moves(board):
    return [i for i in range(9) if board[i] == " "]

# MIN-MAX algorithm with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    result = game_over(board)

    if result is not None:
        if result == "X":
            return -1
        elif result == "O":
            return 1
        else:
            return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves(board):
            board[move] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Find the best move for the AI (O)
def best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False, float('-inf'), float('inf'))
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# main game
def main():
    while True:
        board = init_board()
        player = "X"
        ai = "O"
        introduction = """Welcome to Tic-Tac-Toe!
You are playing against an "unbeatable" opponent.
Try your luck and see if you can defeat it! :-)
"""

        
        print(introduction)
        display_board(board)

        while True:
            if player == "X":
                display_board(board)
                move = int(input("Enter your move from (1-9): ")) - 1
                if move not in available_moves(board):
                    print("Invalid move. Try again.")
                    continue
            else:
                move = best_move(board)

            board[move] = player

            result = game_over(board)
            if result:
                display_board(board)
                if result == "Draw":
                    print("DRAW!")
                else:
                    print(f"{result} wins!")
                break

            player = "X" if player == "O" else "O"

        again = input("Would you like to play another game? (Y/N): ")
        if again.upper() != "Y":
            break

    print("Thanks for playing Tic-Tac-Toe! :-)")

if __name__ == "__main__":
    main()
