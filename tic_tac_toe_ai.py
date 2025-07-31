import math

# Create board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check winner
def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(brd[i] == player for i in condition) for condition in win_conditions)

# Check draw
def is_draw(brd):
    return ' ' not in brd

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    if check_winner(brd, 'X'):
        return -1
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Human move
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Cell already taken.")
        except (IndexError, ValueError):
            print("Invalid input. Try again.")

# Main game loop
def play():
    print("Tic-Tac-Toe: You (X) vs AI (O)")
    print_board()
    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("😔 AI wins!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

play()
