import sys


def search_passes(f):
    seat_ls = []
    for line in f:
        seat_ls.append(str_to_bin(line))
    return seat_ls


def str_to_bin(line):
    max = 0
    line = line.replace('F', '0').replace('L', '0')
    line = line.replace('B', '1').replace('R', '1')
    row = int(line[:7], 2)
    col = int(line[7:], 2)
    return row * 8 + col


def avail_seat(all_seat_ls, seat_ls):
    empty_ls = []
    for seat in all_seat_ls:
        if seat not in seat_ls:
            empty_ls.append(seat)

    for idx, seat in enumerate(empty_ls):
        if seat != idx:
            print(seat)
            break


if __name__ == '__main__':
    all_seat_ls = [i for i in range(0, 1024)]
    with open(sys.argv[1]) as f:
        seat_ls = search_passes(f)
    avail_seat(all_seat_ls, seat_ls)
