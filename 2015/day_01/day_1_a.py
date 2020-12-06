import sys


def floor_count(f):
    for instructions in f:
        instructions = instructions.rstrip()
        print(instructions)
        ups = instructions.count('(')
        downs = instructions.count(')')
        print(str(ups - downs))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        floor_count(f)
