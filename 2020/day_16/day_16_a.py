import sys


def ticket_info(f):
    range_ls = []
    for line in f:
        line = line.rstrip()
        if line == '':
            my_ticket, other_tickets = get_the_rest(f)
            break
        get_ranges(line, range_ls)
    range_ls = list(set(range_ls))
    return my_ticket, other_tickets, range_ls

def get_ranges(line, range_ls):
    cat, ranges = line.split(': ')
    this, that = ranges.split(' or ')
    range_ls += [i for i in range(int(this.split('-')[0]), int(this.split('-')[1])+1)]
    range_ls += [i for i in range(int(that.split('-')[0]), int(that.split('-')[1])+1)]


def get_the_rest(f):
    other_tickets = []
    for idx, line in enumerate(f):
        if idx == 1:
            my_ticket = [int(i) for i in line.rstrip().split(',')]
        elif line[0] in ['n', 'y', '']:
           continue
        elif line == '\n':
           continue
        else:
            other_tickets.append([int(i) for i in line.rstrip().split(',')])
    return my_ticket, other_tickets


def test_tickets(my_ticket, other_tickets, range_ls):
    answer = []
    for ticket in other_tickets:
        for num in ticket:
            if num not in range_ls:
                answer.append(num)
    print(sum(answer))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        my_ticket, other_tickets, range_ls = ticket_info(f)
    test_tickets(my_ticket, other_tickets, range_ls)
