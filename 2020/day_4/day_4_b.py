import re
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
    key_dt = {}
    field_ls = entry.split(' ')
    for field in field_ls:
        key, val = field.split(':')
        key_dt[key] = val
    return(test_fields(key_dt))


def test_fields(key_dt):
    for key in req_fields:
        if key not in key_dt.keys():
            return 0
    passed = new_rules(key_dt)
    return 1 if passed is True else 0


def new_rules(key_dt):
    passed = key_dt['byr'].isdigit() and int(key_dt['byr']) in range(1920, 2002+1)


    if passed is True:
        passed = key_dt['iyr'].isdigit() and int(key_dt['iyr']) in range(2010, 2020+1)


    if passed is True:
        passed = key_dt['eyr'].isdigit() and int(key_dt['eyr']) in range(2020, 2030+1)


    if passed is True:
        hgt_parts = re.findall(r"[^\W\d_]+|\d+", key_dt['hgt'])
        if len(hgt_parts) < 2:
            passed = False
        elif hgt_parts[1] == 'cm':
            passed = int(hgt_parts[0]) in range(150, 193+1)
        elif hgt_parts[1] == 'in':
            passed = int(hgt_parts[0]) in range(59, 76+1)
        else:
            passed = False


    if passed is True:
        for char in key_dt['hcl'][1:]:
            if char not in '0123456789abcdef':
                passed = False
                break
        if passed is True:
            passed = key_dt['hcl'].startswith('#')


    if passed is True:
        passed = key_dt['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


    if passed is True:
        passed = key_dt['pid'].isdigit() and len(key_dt['pid']) == 9


    return passed


if __name__ == '__main__':
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open(sys.argv[1]) as f:
        get_form(f)
