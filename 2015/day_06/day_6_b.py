import numpy as np
import sys

def get_instructions(f):
    grid = make_grid()

    for line in f:
        first, second = line.rstrip().split(' through ')
        first = first.split(' ')
        x_l, y_l, x_r, y_r, rule = get_coords(first, second)
        modify_grid(grid, int(x_l), int(y_l), int(x_r), int(y_r), rule)

    print(np.sum(grid))

def make_grid():
    n = 1000
    return np.zeros([n, n])


def get_coords(first, second):
    x_l, y_l = first[-1].split(',')
    x_r, y_r = second.split(',')
    rule = first[:-1]
    return x_l, y_l, x_r, y_r, rule


def modify_grid(grid, x_l, y_l, x_r, y_r, rule):
    if rule[0] == 'toggle':
        lights_toggle(grid, x_l, y_l, x_r, y_r)
    else:
        lights_on_off(grid, x_l, y_l, x_r, y_r, rule[1])


def lights_on_off(grid, x_l, y_l, x_r, y_r, on):
    on = 1 if on == 'on' else -1
    for x in range(x_l, x_r+1):
        for y in range(y_l, y_r+1):
            if grid[y, x] + on >= 0:
                grid[y, x] = grid[y, x] + on
            else:
                grid[y, x] = 0


def lights_toggle(grid, x_l, y_l, x_r, y_r):
    for x in range(x_l, x_r+1):
        for y in range(y_l, y_r+1):
            grid[y, x] = grid[y, x] + 2


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_instructions(f)

