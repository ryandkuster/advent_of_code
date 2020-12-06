import sys


def get_instructions(f, wire_dt):
    bad_boys = []
    for fileline in f:
        line = fileline.rstrip().split(' ')
        try:
            wire_dt = get_wired(line, wire_dt)
        except KeyError:
            bad_boys.append(fileline)

    while len(bad_boys) > 0:
        get_instructions(bad_boys, wire_dt)

    sys.exit(str(int(wire_dt['a'], 2)))


def get_wired(line, wire_dt):
    if line[1] == '->':
        try:
            bit = get_bit(line)
        except ValueError:
            bit = wire_dt[line[0]]
        wire_dt[line[-1]] = bit

    if line[1] == 'AND':

        if line[0].isdigit():
            var1 = get_bit(line[0])
            output = get_bit_and(var1, wire_dt[line[2]])
        else:
            output = get_bit_and(wire_dt[line[0]], wire_dt[line[2]])
        wire_dt[line[-1]] = output

    if line[1] == 'OR':
        output = get_bit_or(wire_dt[line[0]], wire_dt[line[2]])
        wire_dt[line[-1]] = output

    if line[1] == 'LSHIFT':
        wire_dt[line[-1]] = wire_dt[line[0]][int(line[2]):].ljust(16, '0')

    if line[1] == 'RSHIFT':
        wire_dt[line[-1]] = wire_dt[line[0]][:-int(line[2])].rjust(16, '0')

    if line[0] == 'NOT':
        wire_dt[line[-1]] = ''.join(['1' if i == '0' else '0' for i in wire_dt[line[1]]])

    return wire_dt


def get_bit(line):
    bit = "{0:b}".format(int(line[0])).rjust(16, '0')
    return bit


def get_bit_and(var1, var2):
    output = ''
    for v1, v2 in zip(var1, var2):
        output = output + v2 if v2 == '0' else output + v1
    return output


def get_bit_or(var1, var2):
    output = ''
    for v1, v2 in zip(var1, var2):
        output = output + '0' if v1 == '0' and v2 == '0'  else output + '1'
    return output


if __name__ == '__main__':
    wire_dt = {}
    with open(sys.argv[1]) as f:
        get_instructions(f, wire_dt)
