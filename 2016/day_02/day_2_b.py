import numpy as np
import sys


move_dt = {'L': (-1, 0), 'R': (1, 0), 'D': (0, -1), 'U': (0, 1)}

def starting_grid():
    grid = [['.','.','.','.','.','.','.'],
            ['.','.','.','D','.','.','.'],
            ['.','.','A','B','C','.','.'],
            ['.','5','6','7','8','9','.'],
            ['.','.','2','3','4','.','.'],
            ['.','.','.','1','.','.','.'],
            ['.','.','.','.','.','.','.']]
    return np.array(grid)


def update_grid(grid, press_ls):
    pos = (1, 3)
    xymax = len(grid)
    passcode = ''
    for press in press_ls:
        for move in press:
            x, y = move_dt[move]
            if grid[pos[1]+y][pos[0]+x] != '.':
                pos = tuple(i+j for i, j in zip(pos, (x,y)))
        passcode += str(grid[pos[1]][pos[0]])

    print(passcode)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        press_ls = [[j for j in i.rstrip()] for i in f]

    grid = starting_grid()
    update_grid(grid, press_ls)
