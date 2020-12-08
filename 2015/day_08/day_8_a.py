import re
import sys


def get_lines(f):
    diff_count = 0
    for line in f:
        them = len(line) - 1 - len(eval(line))
        #diff_count += find_non_printed(line.rstrip())
        me = find_non_printed(line.rstrip())
        if them != me:
            print(line, 'them:', them, 'me:', me)
    print(diff_count)


def find_non_printed(line):
    #hex_count = len(re.findall(r'\\x[0-9a-fA-F]{2}', line)) * 3
    hex_count = len(re.findall(r'\\x[0-9a-fA-F]{2}', line)) * 3

    double_count = line.count('\\'*2)

    quote_count = line[:-1].count('\\"')

    return hex_count + double_count + quote_count + 2


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_lines(f)
        #print(sum(len(_) - 1 - len(eval(_)) for _ in f))
