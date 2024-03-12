import random


def display_board(board):

    print('\n' + board[6] + '|' + board[7] + '|' + board[8])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[0] + '|' + board[1] + '|' + board[2])


def player_select():
    marker = ' '
    player2 = ' '

    while marker != 'X' and marker != 'O':
        marker = input('\nPlayer 1 choose X or O: ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def place_marker(board, marker, position):
    if not space_check(board, position-1):
        board[position-1] = marker
        display_board(board)
    else:
        print("Position already occupied. Choose another position.")


def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return True
    else:
        return False


def player_choice(player, board):
    position = 0
    while True:
        position = int(input('\n' + player + '\'s turn (1-9): '))
        if 1 <= position <= 9 and not space_check(board, position - 1):
            break
        else:
            print('Invalid position or position already occupied. Choose another position.')
    return position


def check_winner(board, marker):
    # Check rows, columns, and diagonals for a win
    return (
        (board[0] == board[1] == board[2] == marker) or
        (board[3] == board[4] == board[5] == marker) or
        (board[6] == board[7] == board[8] == marker) or
        (board[0] == board[3] == board[6] == marker) or
        (board[1] == board[4] == board[7] == marker) or
        (board[2] == board[5] == board[8] == marker) or
        (board[0] == board[4] == board[8] == marker) or
        (board[2] == board[4] == board[6] == marker)
    )


def is_board_full(board):
    return ' ' not in board


def game_winner(board):
    if check_winner(board, 'X'):
        return '\nX wins!'
    elif check_winner(board, 'O'):
        return '\nO wins!'
    elif is_board_full(board):
        return '\nIt\'s a tie!'
    else:
        return None


def players_turn(player, board):
    position = player_choice(player, board)
    place_marker(board, player, position)



def playtictactoe():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    print('Welcome to TicTacToe!')

    player1, player2 = player_select()

    random_num = random.randint(0,1)

    first = ' '
    second = ' '

    if random_num == 1:
        first = player1
        second = player2
    elif random_num == 0:
        first = player2
        second = player1

    stop_go = True
    while stop_go:
        position = player_choice(first, board)
        place_marker(board, first, position)

        if game_winner(board):
            print(game_winner(board))
            stop_go = False
            break

        position = player_choice(second, board)
        place_marker(board, second, position)

        if game_winner(board):
            print(game_winner(board))
            stop_go = False
            break

    answer = input('\nDo you wish to play again? ').upper()

    if answer in ['Y', 'YES']:
        playtictactoe()
    else:
        print('\nThanks for playing!')


playtictactoe()