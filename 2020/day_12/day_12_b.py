import sys


move_dt = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
face_dt = {1: 0, 2: 90, 3: 180, 4: 270}
rotate_dt = {1: (1, 1), 2: (1, -1), 3: (-1, -1), 4: (-1, 1)}
sp_pos = (0, 0)
pos = (10, 1)

def navigate(pos, sp_pos, nav):
    if nav[0] in move_dt:
        move = tuple(int(nav[1:])*i for i in move_dt[nav[0]])
        pos = tuple(i+j for i, j in zip(pos, move))

    elif nav[0] == 'F':
        move = tuple(int(nav[1:])*i for i in pos)
        sp_pos = tuple(i+j for i, j in zip(sp_pos, move))

    else:
        mod = 1 if nav[0] == 'R' else -1
        pos = get_quadrant(pos, mod)

    return pos, sp_pos


def get_quadrant(pos, mod):
    if pos[0] >= 0:
        quad = 1 if pos[1] >= 0 else 2
    elif pos[0] < 0:
        quad = 3 if pos[1] < 0 else 4
    degree = (face_dt[quad]+(int(nav[1:])*mod))%360
    rotate = [k for k, v in face_dt.items() if v == degree][0]
    if (rotate-quad)%2 != 0:
        pos = tuple(abs(i)*j for i, j in zip(reversed(pos), rotate_dt[rotate]))
    else:
        pos = tuple(abs(i)*j for i, j in zip(pos, rotate_dt[rotate]))

    return pos


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        nav_ls = [i.rstrip() for i in f]

    for nav in nav_ls:
        pos, sp_pos = navigate(pos, sp_pos, nav)

    print(abs(sp_pos[0]) + abs(sp_pos[1]))

    #higher than 29112
