import itertools
import re
import sys

mem = {}

def get_mask(f):
    for line in f:
        if line.startswith('mask'):
            mask = line.rstrip().split(' = ')[1]
        if line.startswith('mem'):
            idx, val = line.rstrip().split(' = ')
            idx = int(idx.replace('mem[','').replace(']',''))
            mem = apply_mask(mask, idx, val)


def apply_mask(mask, idx, val):
    idx = str(bin(int(idx)))[2:].rjust(36, '0')
    new_val = ''
    for i, j in zip(idx, mask):
        new_val = new_val + j if j != '0' else new_val + i
    new_vals_ls = floaters(new_val)
    for new_val in new_vals_ls:
        mem[int(new_val, 2)] = int(val)


def floaters(new_val):
    new_vals_ls = []
    x_ls = [pos.start() for pos in re.finditer('X', new_val)]
    bin_ls = avoid_itertools(new_val.count('X'))
    for bin in bin_ls:
        newer_val = list(new_val)
        for idx, x in enumerate(x_ls):
            newer_val[x] = bin[idx]
        new_vals_ls.append(''.join(newer_val))
    return new_vals_ls


def avoid_itertools(n):
    bin_ls = []
    for i in range(2**n):
        bin_ls.append(str(bin(i))[2:].rjust(n, '0'))
    return bin_ls


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_mask(f)
    print(sum(mem.values()))
