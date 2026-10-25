board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def game_board(board):
    print(' _____________')
    print(' | ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print(' _____________')
    print(' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print(' _____________')
    print(' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')
    print(' _____________')

def win_check(board, symbol):
    win_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for case in win_cases:
        if board[case[0]] == board[case[1]] == board[case[2]] == symbol:
            return True
    return False


def get_available_positions(board):
    available_positions = []
    for i in range(9):
        if board[i] != 'X' and board[i] != 'O':
            available_positions.append(i)
    return available_positions


print('Hey! Let\'s play Tic-Tac-Toe!!')
print("You are 'X' and the Computer is 'O'")
game_board(board)


def players_turn():
    print('It\'s your turn')
    valid_input = True
    while valid_input:
        entry = int(input('Enter a number(1-9) to choose your position: '))
        index = entry - 1
        if index < 0 or index > 8:
            print('Invalid Entry.Enter a valid number.')
        elif board[index] == 'X' or board[index] == 'O':
            print('Position is occupied.Choose another position.')
        else:
            valid_input = False
    board[index] = 'X'
    game_board(board)
    return valid_input


for turn in range(9):
    available_positions=get_available_positions(board)
    if len(available_positions)==0:
        print("It's a draw.")
        break

    if turn % 2 == 0:
        players_turn()
        if win_check(board, 'X') is True:
            print('Congratulations!!You win!')
            break
    else:
        import random

        print("It's the computer's turn.")
        available_positions = []
        available_positions = get_available_positions(board)
        computer_index = random.choice(available_positions)
        board[computer_index] = 'O'
        game_board(board)
        if win_check(board, 'O'):
            print('Computer wins the game.Better luck next time.')
            break