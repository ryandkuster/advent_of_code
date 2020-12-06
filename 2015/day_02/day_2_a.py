import sys


def get_dims(f):
    sa_ls = []
    for line in f:
        l, w, h = line.rstrip().split('x')
        sa_ls.append(calculate_sa(int(l), int(w), int(h)))
    print(sum(sa_ls))


def calculate_sa(l, w, h):
    sa = [2*l*w, 2*w*h, 2*h*l]
    sa.append(min(sa)/2)
    return sum(sa)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_dims(f)
