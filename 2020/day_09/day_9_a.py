import sys


def check_last_n(xmas, n):
    for idx, i in enumerate(xmas[n:]):
        a_ls = xmas[idx:idx+n]
        b_ls = [i-j if i-j != j else '' for j in a_ls]
        c_ls = [j for j in b_ls if j in a_ls]
        if len(c_ls) == 0:
            return i


if __name__ == '__main__':
    n = 25
    with open(sys.argv[1]) as f:
        xmas = [int(i.rstrip()) for i in f]
    rulebreaker = check_last_n(xmas, n)
    print(rulebreaker)
