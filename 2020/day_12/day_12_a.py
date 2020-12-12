import sys


move_dt = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
face_dt = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
facing = 'E'
pos = (0, 0)

def navigate(pos, facing, nav):
    if nav[0] in move_dt:
        move = tuple(int(nav[1:])*i for i in move_dt[nav[0]])
        pos = tuple(i+j for i, j in zip(pos, move))
    elif nav[0] == 'F':
        move = tuple(int(nav[1:])*i for i in move_dt[facing])
        pos = tuple(i+j for i, j in zip(pos, move))
    else:
        mod = 1 if nav[0] == 'R' else -1
        degree = (face_dt[facing]+(int(nav[1:])*mod))%360
        facing = [k for k, v in face_dt.items() if v == degree][0]

    return pos, facing


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        nav_ls = [i.rstrip() for i in f]

    for nav in nav_ls:
        pos, facing = navigate(pos, facing, nav)

    print(abs(pos[0]) + abs(pos[1]))
