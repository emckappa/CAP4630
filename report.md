# Tic Tac Toe Game with AI
| Author & Developer: Carl Villarosa
Create an unbeatable AI using Minimax Algorithm.

## References

For this project, I used these following sources for understanding TicTacToe with the Minimax Algorithm.

https://www.neverstopbuilding.com/blog/minimax - Jason Fox

https://www.youtube.com/watch?v=8ext9G7xspg - Kylie Ying

## Dependencies

We will use the random module for Python
```Python
pip install random
```

## Start

I will use the basis of Kylie's code for the creation of the program, however I will do it by scratch.

Firstly, I would need to visualize what is needed for a perfect TicTacToe game. 

A computer that would either bring out a draw or a win.

In a short summary, The computer would need to calculate all the possible moves available then use a metric to determine the best possible move.

## Functions

I will need the following functions:

Function | Purpose 
--- | --- 
`init_board` | initialize the tictactoe board 
`display_board` | display the board 
`is_full` | check if the board is full 
`game_over` | check if the game is a win or draw
`available_moves` | get all the available moves 
`minimax` | minimax algo
`best_move` | find best move for AI
`main` | main game


## Problems 


One of the issues I had was adding alpha-beta pruning for my `minimax` function, but ultimately found a solution with after testing

To approach this I have my code using the minimax:

```Python
# Without alpha-beta pruning
def minimax(board, depth, maximizing_player):
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
            eval = minimax(board, depth + 1, False)
            board[move] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = "X"
            eval = minimax(board, depth + 1, True)
            board[move] = " "
            min_eval = min(min_eval, eval)
        return min_eval
```

To optimize the minimax algorithm we would need to apply alpha-beta pruning. This will go into deeper levels and heavily reduce computation time.

In order to implement alpha-beta pruning we will need to add 'alpha' and 'beta' parameters in the function:

```Python
def minimax(board, depth, maximizing_player, alpha, beta):
    result = game_over(board)
```

We will use these parameters for pruning the brances of the game tree that would be irrelevent on the final state.

We also need to add a condition to check if 'beta' is less than or equal to our 'alpha' and will break the loop when it is met.

```Python
# minimax code here
if beta <= alpha:
     break

# some code here

beta = min(beta, eval)
    if beta <= alpha:
     break
```

These conditions are an integral part of the algorithm since we would need them for eliminating branches or nodes of the game tree, giving a much better efficiency.


# Results

![alt text](https://github.com/emckappa/CAP4630/img/1.png?raw=true)

![alt text](https://github.com/emckappa/CAP4630/img/2.png?raw=true)



## Future Improvements

A future improvement I would like to use would be having an interactive GUI to make it visually more appealing. 

As well as including a log and history to view and trace back the player's results.

This is a work in-progress and will be updated soon for more improvements.

