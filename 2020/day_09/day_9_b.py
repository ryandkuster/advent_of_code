import sys


def check_last_n(xmas, n):
    for idx, i in enumerate(xmas[n:]):
        a_ls = xmas[idx:idx+n]
        b_ls = [i-j if i-j != j else '' for j in a_ls]
        c_ls = [j for j in b_ls if j in a_ls]
        if len(c_ls) == 0:
            return i, xmas[:idx+n]


def rulemaker(breaker_ls, rulebreaker):
    for idx1, i in enumerate(breaker_ls):
        for idx2, j in enumerate(breaker_ls[idx1+1:]):
            if sum(breaker_ls[idx1:idx1+idx2+2]) > rulebreaker:
                break
            elif sum(breaker_ls[idx1:idx1+idx2+2]) == rulebreaker:
                return breaker_ls[idx1:idx1+idx2+2]


if __name__ == '__main__':
    n = 25
    with open(sys.argv[1]) as f:
        xmas = [int(i.rstrip()) for i in f]
    rulebreaker, breaker_ls = check_last_n(xmas, n)
    maker_ls = rulemaker(breaker_ls, rulebreaker)
    print(str(min(maker_ls) + max(maker_ls)))
