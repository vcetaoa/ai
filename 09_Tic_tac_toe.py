import random

# Display the board
def display_board(board):
    print('......................................')
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

# Check if a player has won
def win(board, player):
    return win_line(board, player)

def win_line(board, player):
    # Rows
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player):
        return True
    # Columns
    if (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player):
        return True
    # Diagonals
    if (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    return False

# Check if the board is full
def full_board(board):
    return '-' not in board

# Get available moves
def available_moves(board):
    return [i + 1 for i, spot in enumerate(board) if spot == '-']

# Make a move
def make_move(board, move, player):
    board[move - 1] = player

# AI's turn (simple strategy: win, block, or random)
def ai_move(board, player):
    # Check if AI can win
    for move in available_moves(board):
        temp_board = board[:]
        make_move(temp_board, move, player)
        if win(temp_board, player):
            return move
    # Check if AI can block
    opponent = 'o' if player == 'x' else 'x'
    for move in available_moves(board):
        temp_board = board[:]
        make_move(temp_board, move, opponent)
        if win(temp_board, opponent):
            return move
    # Otherwise, choose a random available move
    return random.choice(available_moves(board))

# Game loop
def play_game(board, player):
    display_board(board)
    
    if win(board, 'x'):
        print('Player X wins!')
        return
    if win(board, 'o'):
        print('Player O wins!')
        return
    if full_board(board):
        print('It\'s a draw!')
        return
    
    if player == 'x':
        player_move(board)
        next_player = 'o'
    else:
        move = ai_move(board, 'o')
        make_move(board, move, 'o')
        next_player = 'x'
    
    play_game(board, next_player)

# Player's move
def player_move(board):
    while True:
        try:
            move = int(input('Enter your move (1-9): '))
            if move < 1 or move > 9:
                print('Invalid move. Try again.')
                continue
            if board[move - 1] != '-':
                print('This spot is already taken. Try again.')
                continue
            make_move(board, move, 'x')
            break
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.')

# Start the game
def start_game():
    play_game(['-', '-', '-', '-', '-', '-', '-', '-', '-'], 'x')

# Start the game
start_game()


#OUTPUT:
# python filename.py

#Which Algo used
# Greedy Strategy: AI makes the best decision based on immediate benefits (win or block).
# Search: AI looks one step ahead (win or block).
# Recursion: The game flow is managed using recursion to alternate between players.

# Component 	    Algorithm	                           Key Feature
# Win Check	     Brute-force pattern matching    	Checks all 8 winning combinations
# AI Move	     Greedy heuristic                	Win-block-random priority
# Game Flow	     Recursive state management	        Alternates turns until termination
# Player Input	    Input validation	               Ensures legal moves