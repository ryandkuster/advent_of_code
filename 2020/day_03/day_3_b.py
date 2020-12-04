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
        try:
            tree_ls.append(grid[pos[0], pos[1]%grid_w])
        except IndexError:
            break
        pos = [pos[i] + slope[i] for i, val in enumerate(pos)]
        y += 1
    return tree_ls.count('#')


if __name__ == '__main__':
    tree_counts = []
    with open(sys.argv[1]) as f:
        grid = get_tree_grid(f)
    pos = (0, 0)
    slope_ls = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    for slope in slope_ls:
        tree_counts.append(go_sledding(grid, pos, slope))
    print(np.prod(tree_counts))
