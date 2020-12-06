import sys


def get_quiz(f):
    entry_ls = []
    yes_ls = []
    for line in f:
        if line.startswith('\n'):
            yes_ls.append(get_yes(entry_ls))
            entry_ls = []
            continue
        entry_ls.append(line.rstrip())
    yes_ls.append(get_yes(entry_ls))
    print(sum(yes_ls))


def get_yes(entry_ls):
    yes_count = 0
    yes_all = ''.join(entry_ls)
    yes_set = set(yes_all)
    for char in yes_set:
        if yes_all.count(char) == len(entry_ls):
            yes_count += 1
    return yes_count


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_quiz(f)
