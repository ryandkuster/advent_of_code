import sys


def get_boot(f):
    boot_ls = [op_ls.rstrip().split(' ') for op_ls in f]
    return boot_ls


def check_loop(boot_ls):
    accum = 0
    idx_ls = []
    pos = 0
    while pos not in idx_ls:
        idx_ls.append(pos)
        op, arg = boot_ls[pos]

        if op == 'acc':
            pos += 1
            accum += int(arg)

        if op == 'jmp':
            pos += int(arg)

        if op == 'nop':
            pos += 1

        #print(f'pos: {pos}    accum: {accum}')

    return pos, accum


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        boot_ls = get_boot(f)
    pos, accum = check_loop(boot_ls)
    print(accum)
