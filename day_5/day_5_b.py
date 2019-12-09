import sys


def add_ints(a, b, c, new_code):
    new_code[c] = a + b
    return new_code


def multiply_ints(a, b, c, new_code):
    new_code[c] = a * b
    return new_code


def input_mode(a, new_code):
    input_val = new_code[a]
    return input_val


def output_mode(a, new_code, input_val):
    new_code[a] = input_val
    return new_code


def special_case(code, new_code, i, input_val):
    opcode = str(code)[-2:]
    mode = list(str(code)[:-2][::-1])
    while len(mode) < 3:
        mode.append('0')
    if opcode in ['99']:
        sys.exit()
    elif opcode in ['01', '02']:
        a = new_code[i+1] if mode[0] == '1' else new_code[new_code[i+1]]
        b = new_code[i+2] if mode[1] == '1' else new_code[new_code[i+2]]
        c = new_code[i+3]# if mode[2] == '1' else new_code[new_code[i+3]]
        if opcode == '01':
            new_code = add_ints(a, b, c, new_code)
        if opcode == '02':
            new_code = multiply_ints(a, b, c, new_code)
        next_opcode = i + 4

    elif opcode in ['03', '04']:
        a = new_code[i+1] if mode[0] == '1' else new_code[new_code[i+1]]
        if opcode == '03':
            new_code = output_mode(a, new_code, input_val)
        if opcode == '04':
            input_val = input_mode(a, new_code)
        next_opcode = i + 2

    else:
        sys.exit()

    return new_code, next_opcode


def decoder(intcode):
    input_val = 1
    new_code = intcode
    next_opcode = 0
    for i, code in enumerate(new_code):
        if i == next_opcode:

            if code == 99:
                break

            elif code in [1, 2]:
                a = new_code[new_code[i+1]]
                b = new_code[new_code[i+2]]
                c = new_code[i+3]
                if code == 1:
                    new_code = add_ints(a, b, c, new_code)
                if code == 2:
                    new_code = multiply_ints(a, b, c, new_code)
                next_opcode = i + 4

            elif code == 3:
                new_code = output_mode(new_code[i+1], new_code, input_val)
                next_opcode = i + 2

            elif code == 4:
                input_val = input_mode(new_code[i+1], new_code)
                next_opcode = i + 2

            else:
                new_code, next_opcode = special_case(code, new_code, i, input_val)
    print(input_val)
    print(new_code)


with open(sys.argv[1]) as f:
    for line in f:
        intcode = line.rstrip().split(',')
        intcode = [int(i) for i in intcode]
        decoder(intcode)


