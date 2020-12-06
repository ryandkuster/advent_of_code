import sys


def get_list(f):
    nice_ls = []
    for line in f:
        nice_ls.append(nice_check(line.rstrip()))
    print(sum(nice_ls))


def nice_check(line):
    double, spacer = False, False

    for idx, char in enumerate(line):

        if idx < len(line) - 1:
            if line.count(line[idx:idx+2]) > 1:
                double = True

        if idx < len(line) - 2:
            if line[idx+2] == char:
                spacer = True

    return 1 if double and spacer else 0


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_list(f)
