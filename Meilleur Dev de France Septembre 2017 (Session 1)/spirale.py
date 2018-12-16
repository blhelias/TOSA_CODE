# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 20:59:39 2018

@author: brieuc
"""

from collections import namedtuple
Coor = namedtuple('coor', ['X', 'Y'])


def vertical(coor, board, n, down=True):
    if down:
        for i in range(coor.X, coor.X+(n+1)):
            board[i][coor.Y] = 1
            last_coor = Coor(i, coor.Y)
    else:
        for i in range(coor.X, coor.X-(n+1), -1):
            board[i][coor.Y] = 1
            last_coor = Coor(i, coor.Y)
    return board, last_coor


def horizontal(coor, board, n, right=True):
    if right:
        for i in range(coor.Y, coor.Y+(n+1)):
            board[coor.X][i] = 1
            last_coor = Coor(coor.X, i)
    else:
        for i in range(coor.Y, coor.Y-(n+1), -1):
            board[coor.X][i] = 1
            last_coor = Coor(coor.X, i)
    return board, last_coor


if __name__ == "__main__":
    # lines = []
    # for line in sys.stdin:
    # lines.append(line.rstrip('\n'))
    #
    # n = lines[0]

    # INIT #
    turn = 0
    count = 0
    n = 5
    board = [[0 for i in range(n)] for i in range(n)]
    board[n//2][n//2] = 1
    coor = Coor(n//2, n//2)
    # INIT #

    while True:
        # check horizontal
        if turn == 0:  # check horizontal left
            if (coor.Y - (count + 1)) >= 0:
                board, coor = horizontal(coor, board, count+1, right=False)
            else:
                board, coor = horizontal(coor, board, count, right=False)
               
        elif turn == 2:  # check horizontal right
            if (coor.Y + (count + 1)) < n:
                board, coor = horizontal(coor, board, count+1)
            else:
                board, coor = horizontal(coor, board, count)
               
        # check vertical
        elif turn == 1:
            if (coor.X + (count + 1)) < n:
                board, coor = vertical(coor, board, count+1)
            else:
                board, coor = vertical(coor, board, count)
               
        elif turn == 3:
            if (coor.X - (count + 1)) >= 0:
                board, coor = vertical(coor, board, count+1, down=False)
            else:
                board, coor = vertical(coor, board, count, down=False)
                
        if turn == 3:
            turn = 0
        else:
            turn += 1
        count += 1
        
    print(board)
    print()
    for row in board:
        for col in row:
            if col == 0:
                print("=", end="")
            else:
                print("#", end="")
                
        print()
        
