import sys


def get_path(f):
    dir_dt = {'^': (0, 1),
              'v': (0, -1),
              '<': (-1, 0),
              '>': (1, 0)}
    for path in f:
        comb_ls = []
        santa_path, rob_path = robo_paths(path.rstrip())
        comb_ls += path_maker(santa_path, dir_dt)
        comb_ls += path_maker(rob_path, dir_dt)
        print(len(set(comb_ls)))


def robo_paths(path):
    santa_path = [char for idx, char in enumerate(path) if idx%2 == 0]
    rob_path = [char for idx, char in enumerate(path) if idx%2 != 0]
    return santa_path, rob_path


def path_maker(path, dir_dt):
    pos_ls = [(0, 0)]
    for direction in path:
        pos_ls.append(tuple(map(sum, zip(pos_ls[-1], dir_dt[direction]))))
    return pos_ls


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_path(f)
