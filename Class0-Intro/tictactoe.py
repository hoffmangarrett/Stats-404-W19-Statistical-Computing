import numpy


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-----------------------')


board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}
vertical = {0: 'top', 1: 'mid', 2: 'low'}
horizontal = {0: 'L', 1: 'M', 2: 'R'}
moves = numpy.random.permutation(range(9))
xmoves = set()
omoves = set()


def win(moves):
    return (
            set([0, 1, 2]).issubset(moves) or
            set([3, 4, 5]).issubset(moves) or
            set([6, 7, 8]).issubset(moves) or
            set([0, 3, 6]).issubset(moves) or
            set([1, 4, 7]).issubset(moves) or
            set([2, 5, 8]).issubset(moves) or
            set([0, 4, 8]).issubset(moves) or
            set([2, 4, 6]).issubset(moves)
    )


for i in range(10):
    if (win(xmoves)):
        print('Player X wins!')
        break
    elif (win(omoves)):
        print('Player O wins!')
        break
    elif (i > 8):
        print('Cats Game - No player wins!')
        break
    else:
        move = moves[i]
        square = vertical[move//3] + '-' + horizontal[move%3]
        if i%2 == 0:
            xmoves.add(move)
            board[square] = 'X'
        else:
            omoves.add(move)
            board[square] = 'O'
    printBoard(board)
