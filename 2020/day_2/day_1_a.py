import sys


def pass_policies(f):
    good_count = 0
    for line in f:
        p, let, pword = line.rstrip().split(' ')
        pol = list(map(int, p.split('-')))
        good_count = pass_testing(pol, let[0], pword, good_count)
    print(good_count)


def pass_testing(pol, let, pword, good_count):
    check = pword.count(let)
    if check in range(pol[0], pol[1]+1):
        good_count += 1
    return good_count


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        pass_policies(f)
