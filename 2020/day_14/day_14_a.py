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
    val = str(bin(int(val)))[2:].rjust(36, '0')
    new_val = ''
    for i, j in zip(val, mask):
        new_val = new_val + j if j != 'X' else new_val + i
    mem[idx] = (int(new_val, 2))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_mask(f)
    print(sum(mem.values()))
