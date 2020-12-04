import numpy as np
import sys


def get_tree_grid(f):
    for count, line in enumerate(f):
        row = list(line.rstrip())
        if count == 0:
            grid = np.array(row)
        else:
            grid = np.vstack((grid, row))
    return grid


def go_sledding(grid, pos, slope):
    y = 0
    grid_l = grid.shape[0]
    grid_w = grid.shape[1]
    tree_ls = []
    while y < grid_l:
        tree_ls.append(grid[pos[0], pos[1]%grid_w])
        pos = [pos[i] + slope[i] for i, val in enumerate(pos)]
        y += 1
    return tree_ls


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        grid = get_tree_grid(f)
    pos = (0, 0)
    slope = (1, 3)
    tree_ls = go_sledding(grid, pos, slope)
    print(tree_ls.count('#'))
