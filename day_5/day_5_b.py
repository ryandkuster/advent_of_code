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
    elif opcode in ['01', '02', '07', '08']:
        a = new_code[i+1] if mode[0] == '1' else new_code[new_code[i+1]]
        b = new_code[i+2] if mode[1] == '1' else new_code[new_code[i+2]]
        c = new_code[i+3]# if mode[2] == '1' else new_code[new_code[i+3]]
        if opcode == '01':
            new_code = add_ints(a, b, c, new_code)
        if opcode == '02':
            new_code = multiply_ints(a, b, c, new_code)
        if opcode == '07':
            new_code[c] = 1 if new_code[a] < new_code[b] else 0
        if opcode == '08':
            new_code[c] = 1 if new_code[a] == new_code[b] else 0
        next_opcode = i + 4

    elif opcode in ['03', '04']:
        a = new_code[i+1] if mode[0] == '1' else new_code[new_code[i+1]]
        if opcode == '03':
            new_code = output_mode(a, new_code, input_val)
        if opcode == '04':
            input_val = input_mode(a, new_code)
        next_opcode = i + 2

    elif opcode in ['05', '06']:
        if opcode == '05':
            next_opcode = new_code[i+2] if new_code[i+1] != 0 else i + 3
        if opcode == '06':
            next_opcode = new_code[i+2] if new_code[i+1] == 0 else i + 3

    return new_code, next_opcode


def decoder(new_code, i, input_val):
    code = new_code[i]
    if code == 99:
        return new_code, input_val

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
 
    elif code == 5:
        if new_code[i+1] != 0:
            next_opcode = new_code[i+2]
        else:
            next_opcode = i + 3
 
    elif code == 6:
        if new_code[i+1] == 0:
            next_opcode = new_code[i+2]
        else:
            next_opcode = i + 3

    elif code == 7:
        new_code[new_code[i+3]] = 1 if new_code[i+1] < new_code[i+2] else 0
        next_opcode = i + 4
 
    elif code == 8:
        new_code[new_code[i+3]] = 1 if new_code[i+1] == new_code[i+2] else 0
        next_opcode = i + 4

    else:
        new_code, next_opcode = special_case(code, new_code, i, input_val)
    new_code, input_val = decoder(new_code, next_opcode, input_val)
    return new_code, input_val

input_val = int(sys.argv[2])
with open(sys.argv[1]) as f:
    for line in f:
        intcode = line.rstrip().split(',')
        intcode = [int(i) for i in intcode]
        new_code, input_val = decoder(intcode, 0, input_val)
        print(new_code)
        print(input_val)

