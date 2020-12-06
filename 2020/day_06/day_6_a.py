import sys


def get_quiz(f):
    entry = ''
    yes_ls = []
    for line in f:
        if line.startswith('\n'):
            yes_ls.append(get_yes(entry))
            entry = ''
            continue
        entry += line.rstrip()
    yes_ls.append(get_yes(entry))
    print(sum(yes_ls))


def get_yes(entry):
    return len(set(entry))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_quiz(f)
