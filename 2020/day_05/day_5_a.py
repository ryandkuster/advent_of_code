import sys


def search_passes(f):
    max = 0
    for line in f:
        seat = str_to_bin(line)
        max = seat if seat > max else max
    print(max)


def str_to_bin(line):
    max = 0
    line = line.replace('F', '0').replace('L', '0')
    line = line.replace('B', '1').replace('R', '1')
    row = int(line[:7], 2)
    col = int(line[7:], 2)
    return row * 8 + col


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        search_passes(f)
