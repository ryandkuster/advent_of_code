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

            tl = traverse(grid, xmax, ymax, x, y, -1, -1)
            tm = traverse(grid, xmax, ymax, x, y, 0, -1)
            tr = traverse(grid, xmax, ymax, x, y, 1, -1)
            ml = traverse(grid, xmax, ymax, x, y, -1, 0)
            mr = traverse(grid, xmax, ymax, x, y, 1, 0)
            bl = traverse(grid, xmax, ymax, x, y, -1, 1)
            bm = traverse(grid, xmax, ymax, x, y, 0, 1)
            br = traverse(grid, xmax, ymax, x, y, 1, 1)
            adjacent = tl + tm + tr + ml + mr + bl + bm + br

            if grid[y][x] == 'L' and adjacent.count('#') == 0:
                new_grid[y][x] = '#'

            if grid[y][x] == '#' and adjacent.count('#') >= 5:
                new_grid[y][x] = 'L'

    stable = True if np.array_equal(grid, new_grid) else False
    return new_grid, stable


def traverse(grid, xmax, ymax, xpos, ypos, xchange, ychange):
    xpos += xchange
    ypos += ychange
    while xpos in range(0, xmax) and ypos in range(0, ymax):
        target = grid[ypos][xpos]
        if target == '#':
            return '#'
        elif target == 'L':
            return 'L'
        xpos += xchange
        ypos += ychange
    return '0'


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        grid = starting_grid(f)
    new_grid, stable = update_grid(grid)
    while stable is not True:
        new_grid, stable = update_grid(new_grid)
    print(np.count_nonzero(new_grid == '#'))
