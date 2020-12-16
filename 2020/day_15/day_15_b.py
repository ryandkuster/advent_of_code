import sys


def makin_a_list(the_list):
    for i in range(30000000-len(the_list)):
        if the_list[-1] not in the_list[:-1]:
            the_list.append(0)
        else:
            the_list.append(list(reversed(the_list[:-1])).index(the_list[-1])+1)
    print(the_list[-1])


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            the_list = line.rstrip().split(',')
            the_list = [int(i) for i in the_list]
            makin_a_list(the_list)
