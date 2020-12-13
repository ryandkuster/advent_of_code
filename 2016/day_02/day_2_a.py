import numpy as np
import sys


move_dt = {'L': [(-1, 0), 0], 'R': [(1, 0), 2], 'D': [(0, -1), 0], 'U': [(0, 1), 2]}

def starting_grid():
    grid = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    return np.array(grid)


def update_grid(grid, press_ls):
    pos = (1, 1)
    xymax = len(grid)
    passcode = ''
    for press in press_ls:
        for move in press:
            move_type = move_dt[move]
            pos = tuple(i+j if i+j in range(0, 3) else move_type[1] for i, j in zip(pos, move_type[0]))
        passcode += str(grid[pos[1]][pos[0]])

    print(passcode)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        press_ls = [[j for j in i.rstrip()] for i in f]

    grid = starting_grid()
    update_grid(grid, press_ls)
