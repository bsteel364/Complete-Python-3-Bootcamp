# Terminal Tic-Tac-Toe
# Brandon Steel


def draw_board(board):
    print('{}'.format(board[7]) + '|' + '{}'.format(board[7]) + '|' + '{}'.format(board[7]))
    print('-------')
    print('{}'.format(board[4]) + '|' + '{}'.format(board[5]) + '|' + '{}'.format(board[6]))
    print('-------')
    print('{}'.format(board[1]) + '|' + '{}'.format(board[2]) + '|' + '{}'.format(board[3]))
    print('\n\n')

def X_move():
    legalmove = False
    while legalmove is False:
        move = int(input("X's turn: "))
        if move in [1, 2, 3, 4, 5, 6, 7, 8, 9] and board_data[move] == ' ':
            legalmove = True
            board_data[move] = 'X'
        else:
            move = input('Invalid move: try again: ')


def O_move():
    legalmove = False
    while legalmove is False:
        move = int(input("O's turn: "))
        if move in [1, 2, 3, 4, 5, 6, 7, 8, 9] and board_data[move] == ' ':
            legalmove = True
            board_data[move] = 'O'
        else:
            move = input('Invalid move: try again: ')


def X_win():
    if board_data[1] == 'X' and board_data[2] == 'X' and board_data[3] == 'X':
        return True
    if board_data[4] == 'X' and board_data[5] == 'X' and board_data[6] == 'X':
        return True
    if board_data[7] == 'X' and board_data[8] == 'X' and board_data[9] == 'X':
        return True
    if board_data[1] == 'X' and board_data[4] == 'X' and board_data[7] == 'X':
        return True
    if board_data[2] == 'X' and board_data[5] == 'X' and board_data[8] == 'X':
        return True
    if board_data[3] == 'X' and board_data[6] == 'X' and board_data[9] == 'X':
        return True
    if board_data[1] == 'X' and board_data[5] == 'X' and board_data[9] == 'X':
        return True
    if board_data[3] == 'X' and board_data[5] == 'X' and board_data[7] == 'X':
        return True
    else:
        return False


def O_win():
        if board_data[1] == 'O' and board_data[2] == 'O' and board_data[3] == 'O':
            return True
        if board_data[4] == 'O' and board_data[5] == 'O' and board_data[6] == 'O':
            return True
        if board_data[7] == 'O' and board_data[8] == 'O' and board_data[9] == 'O':
            return True
        if board_data[1] == 'O' and board_data[4] == 'O' and board_data[7] == 'O':
            return True
        if board_data[2] == 'O' and board_data[5] == 'O' and board_data[8] == 'O':
            return True
        if board_data[3] == 'O' and board_data[6] == 'O' and board_data[9] == 'O':
            return True
        if board_data[1] == 'O' and board_data[5] == 'O' and board_data[9] == 'O':
            return True
        if board_data[3] == 'O' and board_data[5] == 'O' and board_data[7] == 'O':
            return True
        else:
            return False


# ====== Program Start =======
board_data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
victory = False
turns = 0
while victory is False:
    draw_board(board_data)
    O_move()
    turns = turns + 1
    if O_win():
        print('O wins')
        draw_board(board_data)
        break
    if turns == 9:
        print("game over")
        break
    draw_board(board_data)
    X_move()
    turns = turns + 1
    if X_win():
        print('X wins')
        draw_board(board_data)
        break
    if turns == 9:
        print("game over")
        break