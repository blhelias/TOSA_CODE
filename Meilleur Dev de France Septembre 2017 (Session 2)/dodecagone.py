"""
Let's say we have an input of N=9

the output should look as follow;

    .#######.
    ##*****##
    #**###**#
    #*##*##*#
    #*#***#*#
    #*##*##*#
    #**###**#
    ##*****##
    .#######.
"""
N = 9
grid = [["." for i in range(N)] for j in range(N)]

def print_grille(grid):
   for i in range(N):
       # print(end=" ")
       print()
       for j in range(N):
           print(grid[i][j], end="")

def draw(grid):
    shapes = [".", "#", "*"]
    row_start = 0
    col_start = 0
    col_len = N
    row_len = N
    tour = 1

    for i in range(N-1):

        for droite in range(row_start, col_len):
            grid[row_start][droite] = shapes[tour]

        for gauche in range(col_len-1, col_start, -1):
            grid[row_len-1][gauche] = shapes[tour]

        for bas in range(row_start+1, row_len):
            grid[bas][col_len-1] = shapes[tour]

        for haut in range(row_len-1, row_start, -1):
            grid[haut][col_start] = shapes[tour]

        if i == 0:
            grid[row_start][col_start] = shapes[0]
            grid[row_start][col_len-1] = shapes[0]
            grid[row_len-1][col_start] = shapes[0]
            grid[row_len-1][col_len-1] = shapes[0]
        else:
            grid[row_start][col_start] = shapes[3-tour]
            grid[row_start][col_len-1] = shapes[3-tour]
            grid[row_len-1][col_start] = shapes[3-tour]
            grid[row_len-1][col_len-1] = shapes[3-tour]

        row_start += 1
        col_start += 1
        row_len -= 1
        col_len -= 1
        tour = 3 - tour

    return grid

print_grille(draw(grid))




