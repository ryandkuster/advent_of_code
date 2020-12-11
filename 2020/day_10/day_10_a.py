import sys


def count_jumps(jolt_ls):
    total_ls = []
    for idx, i in enumerate(jolt_ls[1:]):
        total_ls.append(i - jolt_ls[idx])
    print(total_ls.count(1) * total_ls.count(3))


if __name__ == '__main__':
    jolt_ls = [0]
    with open(sys.argv[1]) as f:
        jolt_ls += [int(i.rstrip()) for i in f]
    jolt_ls.sort()
    jolt_ls.append(max(jolt_ls) + 3)
    count_jumps(jolt_ls)
