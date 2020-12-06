import sys


def get_list(f):
    nice_ls = []
    for line in f:
        nice_ls.append(nice_check(line.rstrip()))
    print(sum(nice_ls))


def nice_check(line):
    if len([i for i in line if i in 'aeiou']) < 3:
        return 0
    if len([i for i in line if i*2 in line]) < 1:
        return 0
    if len([i for i in ['ab', 'cd', 'pq', 'xy'] if i in line]) > 0:
        return 0
    return 1


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_list(f)
