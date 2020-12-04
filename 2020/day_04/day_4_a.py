import sys


def get_form(f):
    entry = ''
    okay_pass = 0
    for line in f:
        if line.startswith('\n'):
            okay_pass += get_fields(entry[:-1])
            entry = ''
            continue
        entry += line.rstrip() + ' '
    okay_pass += get_fields(entry[:-1])
    print(okay_pass)


def get_fields(entry):
    key_ls = []
    field_ls = entry.split(' ')
    for field in field_ls:
        key, val = field.split(':')
        key_ls.append(key)
    return(test_fields(key_ls))


def test_fields(key_ls):
    for key in req_fields:
        if key not in key_ls:
            return 0
    return 1


if __name__ == '__main__':
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open(sys.argv[1]) as f:
        get_form(f)
