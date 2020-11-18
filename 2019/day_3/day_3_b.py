import sys


def framemaker(wire):
    path = [[0,0]]
    for idx, i in enumerate(wire):
        current = path[-1]
        x, extend, step = coordinate(i)
        if x is True:
            end = current[0] + extend
            for j in range(current[0]+step, end+step, step):
                path.append([j, current[1]])
        if x is False: 
            end = current[1] + extend
            for j in range(current[1]+step, end+step, step):
                path.append([current[0], j])
    return path[1:]


def coordinate(entry):
    direction = entry[0]
    extend = int(entry[1:])
    if direction == 'U':
        return False, extend, 1
    if direction == 'D':
        return False, -extend, -1
    if direction == 'L':
        return True, -extend, -1
    if direction == 'R':
        return True, extend, 1


with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i == 0:
            wire1 = line.rstrip().split(',')
        if i == 1:
            wire2 = line.rstrip().split(',')

print('finding wire1 path')
path1 = framemaker(wire1)
print('finding wire2 path')
path2 = framemaker(wire2)

print('finding the shortest path of intersection')
min_steps = 1e23
for x, i in enumerate(path1):
    if i in path2:
        temp_steps = x + path2.index(i) + 2
        if temp_steps < min_steps:
            min_steps = temp_steps

print(min_steps)


