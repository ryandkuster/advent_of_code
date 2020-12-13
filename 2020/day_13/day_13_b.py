import sys


def bus_loop(bus_ls):
    time = 0
    jump = 1

    while True:
        time += jump
        compat_ls = []
        for idx, bus in enumerate(bus_ls):
            if (time + idx) % bus == 0:
                compat_ls.append(bus)
        result = 1
        for i in compat_ls:
            result = result * i
        jump = result
        if bus_ls == compat_ls:
            return time


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        _ = float(f.readline().rstrip())
        bus_ls = f.readline().rstrip().split(',')
    bus_ls = [int(i) if i != 'x' else 1 for i in bus_ls]
    time = bus_loop(bus_ls)
    print(time)
