import sys


def get_path(f):
    dir_dt = {'^': (0, 1),
              'v': (0, -1),
              '<': (-1, 0),
              '>': (1, 0)}
    for path in f:
        path_maker(path.rstrip(), dir_dt)


def path_maker(path, dir_dt):
    pos_ls = [(0, 0)]
    for direction in path:
        pos_ls.append(tuple(map(sum, zip(pos_ls[-1], dir_dt[direction]))))
    print(len(set(pos_ls)))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_path(f)
