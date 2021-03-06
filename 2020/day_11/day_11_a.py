import numpy as np
import sys


def starting_grid(f):
    grid = []
    for line in f:
        grid.append([i for i in line.rstrip()])
    return np.array(grid)


def update_grid(grid):
    new_grid = grid.copy()
    xmax = len(grid[0])
    ymax = len(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):

            if grid[y][x] == '.':
                continue

            tl = grid[y-1][x-1] if x-1 in range(0, xmax) and y-1 in range(0, ymax) else '0'
            tm = grid[y-1][x] if x in range(0, xmax) and y-1 in range(0, ymax) else '0'
            tr = grid[y-1][x+1] if x+1 in range(0, xmax) and y-1 in range(0, ymax) else '0'
            ml = grid[y][x-1] if x-1 in range(0, xmax) and y in range(0, ymax) else '0'
            mr = grid[y][x+1] if x+1 in range(0, xmax) and y in range(0, ymax) else '0'
            bl = grid[y+1][x-1] if x-1 in range(0, xmax) and y+1 in range(0, ymax) else '0'
            bm = grid[y+1][x] if x in range(0, xmax) and y+1 in range(0, ymax) else '0'
            br = grid[y+1][x+1] if x+1 in range(0, xmax) and y+1 in range(0, ymax) else '0'
            adjacent = tl + tm + tr + ml + mr + bl + bm + br

            if grid[y][x] == 'L' and adjacent.count('#') == 0:
                new_grid[y][x] = '#'

            if grid[y][x] == '#' and adjacent.count('#') >= 4:
                new_grid[y][x] = 'L'

    stable = True if np.array_equal(grid, new_grid) else False
    return new_grid, stable


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        grid = starting_grid(f)
    new_grid, stable = update_grid(grid)
    while stable is not True:
        new_grid, stable = update_grid(new_grid)
    print(np.count_nonzero(new_grid == '#'))
