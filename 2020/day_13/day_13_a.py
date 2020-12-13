import sys


def bus_loop(time, bus_ls):
    while True:
        for bus in bus_ls:
            f = time / bus
            if f.is_integer():
                return bus, time
        time += 1


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        early = float(f.readline().rstrip())
        bus_ls = f.readline().rstrip().split(',')
    bus_ls = [int(i) for i in bus_ls if i != 'x']
    bus, time = bus_loop(early, bus_ls)
    print(bus * (int(time) - int(early)))
