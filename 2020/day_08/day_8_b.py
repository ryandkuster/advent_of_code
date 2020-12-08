import copy
import sys


def get_boot(f):
    boot_ls = [op_ls.rstrip().split(' ') for op_ls in f]
    return boot_ls


def brute_force(boot_ls):
    brute_ls = []
    for idx, i in enumerate(boot_ls):

        if i[0] == 'jmp':
            tmp_boot_ls = copy.deepcopy(boot_ls)
            tmp_boot_ls[idx][0] = 'nop'
            brute_ls.append(tmp_boot_ls)
        elif i[0] == 'nop':
            tmp_boot_ls = copy.deepcopy(boot_ls)
            tmp_boot_ls[idx][0] = 'jmp'
            brute_ls.append(tmp_boot_ls)

    return brute_ls


def check_loop(boot_ls):
    accum = 0
    idx_ls = []
    pos = 0
    while pos not in idx_ls:
        curr_pos = pos
        idx_ls.append(pos)
        op, arg = boot_ls[pos]

        if op == 'acc':
            pos += 1
            accum += int(arg)

        if op == 'jmp':
            pos += int(arg)

        if op == 'nop':
            pos += 1

        if curr_pos == len(boot_ls)-1:
            return True, accum

    return False, accum


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        boot_ls = get_boot(f)
    brute_ls = brute_force(boot_ls)
    for i in brute_ls:
        test, accum = check_loop(i)
        if test is True:
            break
    print(accum)
