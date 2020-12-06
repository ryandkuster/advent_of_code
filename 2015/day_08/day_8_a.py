import re
import sys


def get_lines(f):
    diff_count = 0
    for line in f:
        diff_count += find_non_printed(line.rstrip())
    print(diff_count)


def find_non_printed(line):
    hex_count = len(re.findall (r'\\x[0-9a-fA-F]+', line)) * 3
    #print(hex_count, 'hex')

    double_count = line.count('\\'*2) * 2
    #print(double_count, 'doubles')

    quote_count = line.count('\\"')
    #print(quote_count, 'quotes')

    return hex_count + double_count + quote_count + 2


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_lines(f)
