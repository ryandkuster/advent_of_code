import sys


def floor_count(f):
    for instructions in f:
        instructions = instructions.rstrip()
        iter_count(instructions)


def iter_count(instructions):
    floor = 0
    for idx, char in enumerate(instructions):
        floor = floor + 1 if char == '(' else floor - 1
        if floor == -1:
            print(str(idx+1))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        floor_count(f)
