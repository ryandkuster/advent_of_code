import sys


def get_dims(f):
    ribbon_ls = []
    for line in f:
        l, w, h = line.rstrip().split('x')
        ribbon_ls.append(calculate_perim(int(l), int(w), int(h)))
        ribbon_ls.append(int(l) * int(w) * int(h))
    print(sum(ribbon_ls))


def calculate_perim(l, w, h):
    dim_ls = sorted([l, w, h])
    dim_ls = dim_ls[:-1]
    dim_ls = dim_ls * 2
    return sum(dim_ls)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_dims(f)
