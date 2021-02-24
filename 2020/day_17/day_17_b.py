import copy
import numpy as np
import sys


def wrap_slice(slice):
    '''
    slab is z axis in either direction
    '''
    extend = len(slice[0]) + 2
    slab = [['.' for i in range(extend)] for i in range(extend)]
    wrapped_slice = [copy.deepcopy(slab)]
    for z in slice:
        #add the new top row from slab
        new_z = [copy.deepcopy(slab[0])]
        for y in z:
            new_z.append(['.'] + copy.deepcopy(y) + ['.'])
        new_z.append(copy.deepcopy(slab[0]))
        wrapped_slice.append(new_z)
    wrapped_slice.append(copy.deepcopy(slab))
    return wrapped_slice


#def wrap_slice(slice):
#    '''
#    slab is z axis in either direction
#    '''
#    extend = len(slice[0]) + 2
#    slab = [['.' for i in range(extend)] for i in range(extend)]
#    slice = [['.']+i+[','] for i in slice]
#    slice.insert(0, copy.deepcopy(slab[0]))
#    slice.append(copy.deepcopy(slab[0]))
#    slice = [slab, slice, slab]
#    return slice


def update_grid(slice):
    slice_copy = copy.deepcopy(slice)
    for z, zl in enumerate(slice):
        for y, yl in enumerate(zl):
            for x, xl in enumerate(yl):
                slice_copy = check_surroundings(slice, slice_copy, z, y, x)
    return copy.deepcopy(slice_copy)


def check_surroundings(slice, slice_copy, z, y, x):
    neighbors = []
    for z2 in range(len(slice)):
        for y2 in range(len(slice[z2])):
            for x2 in range(len(slice[z2][y2])):
                if z2 in range(z-1, z+2) and y2 in range(y-1, y+2) and x2 in range(x-1, x+2):
                    if (z2, y2, x2) == (z, y, x):
                        continue
                    else:
                        neighbors.append(slice[z2][y2][x2])

    if slice[z][y][x] == '#' and neighbors.count('#') not in range(2, 4):
        slice_copy[z][y][x] = '.'
    if slice[z][y][x] == '.' and neighbors.count('#') == 3:
        slice_copy[z][y][x] = '#'

    return slice_copy


def count_active(slice):
    total = 0
    for z in slice:
        for y in z:
            total += y.count('#')
    print(total)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        slice = [[list(line.rstrip()) for line in f]]
    for i in range(6):
        print(i)
        slice = wrap_slice(slice)
        slice = update_grid(slice)
    count_active(slice)
