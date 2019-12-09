import sys


def add_ints(a, b, c, new_code):
    try:
        new_code[c] = new_code[a] + new_code[b]
    except IndexError:
        return False
    return new_code


def multiply_ints(a, b, c, new_code):
    try:
        new_code[c] = new_code[a] * new_code[b]
    except IndexError:
        return False
    return new_code


def decoder(bentcode, noun, verb):
    bentcode[1] = noun
    bentcode[2] = verb
    new_code = bentcode.copy()
    for i, code in enumerate(bentcode):
        if (i + 4)%4 == 0:
            if code == 99:
                break
            elif code == 1:
                new_code = add_ints(*new_code[i+1:i+4], new_code)
                if new_code is False:
                    break
            elif code == 2:
                new_code = multiply_ints(*new_code[i+1:i+4], new_code)
                if new_code is False:
                    break
            else:
                break
    if new_code is not False:
        if new_code[0] == 19690720:
            print('noun :', noun)
            print('verb :', verb)
            print(100 * noun + verb)
            sys.exit()


with open(sys.argv[1]) as f:
    for line in f:
        intcode = line.rstrip().split(',')
        intcode = [int(i) for i in intcode]

for noun in range(1, 1000):
    bentcode = intcode.copy()
    for verb in range(1, 1000):
        decoder(bentcode, noun, verb)


