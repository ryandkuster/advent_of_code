import sys


def makin_a_list(the_list):
    the_dt = {i:idx for idx, i in enumerate(the_list)}
    spot = 0
    for i in range(len(the_list), 30000000-1):
        if spot in the_dt:
            new_spot = i - the_dt[spot]
        else:
            new_spot = 0
        the_dt[spot] = i
        spot = new_spot
    print(spot)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            the_list = line.rstrip().split(',')
            the_list = [int(i) for i in the_list]
            makin_a_list(the_list)
