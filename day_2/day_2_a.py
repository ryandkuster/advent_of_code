import sys


def add_ints(a, b, c, new_code):
    new_code[c] = new_code[a] + new_code[b]
    return new_code


def multiply_ints(a, b, c, new_code):
    new_code[c] = new_code[a] * new_code[b]
    return new_code


def decoder(intcode):
    print(intcode)
    new_code = intcode
    for i, code in enumerate(intcode):
        if (i + 4)%4 == 0:
            if code == 99:
                break
            elif code == 1:
                new_code = add_ints(*new_code[i+1:i+4], new_code)
            elif code == 2:
                new_code = multiply_ints(*new_code[i+1:i+4], new_code)
            else:
                break
    print(new_code)


with open(sys.argv[1]) as f:
    for line in f:
        intcode = line.rstrip().split(',')
        intcode = [int(i) for i in intcode]
        intcode[1] = 12
        intcode[2] = 2
        decoder(intcode)


