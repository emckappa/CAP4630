"""
Tic Tac Toe using MinMax algorithm

A text-based Tic-Tac-Toe game where you can play against an AI opponent. Try to outsmart the AI and win the game!

Author: Carl Villarosa
cvillarosa2022@fau.edu
"""

import random


# Initialize the Tic-Tac-Toe board
def init_board():
    return [" " for _ in range(9)]

# Display the Tic-Tac-Toe board
def display_board(board):
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-----------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")

# Check if the board is full
def is_full(board):
    return " " not in board

# Check if the game is over (win or draw)
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
        return "Draw"
    
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

# Main game loop
def main():
    while True:
        board = init_board()
        player = "X"
        ai = "O"

        print("Welcome to Tic-Tac-Toe!")
        display_board(board)

        while True:
            if player == "X":
                display_board(board)
                move = int(input("Enter your move (1-9): ")) - 1
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

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thank you for playing Tic-Tac-Toe!")

if __name__ == "__main__":
    main()
