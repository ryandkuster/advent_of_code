import pandas as pd
import sys


def ticket_info(f):
    range_ls = []
    cat_dt = {}
    colnames = []
    for line in f:
        line = line.rstrip()
        if line == '':
            my_ticket, other_tickets = get_the_rest(f)
            break
        get_ranges(line, cat_dt, range_ls, colnames)
    range_ls = list(set(range_ls))
    df = pd.DataFrame(columns=colnames)
    return my_ticket, other_tickets, range_ls, cat_dt, df


def get_ranges(line, cat_dt, range_ls, colnames):
    tmp_ls = []
    cat, ranges = line.split(': ')
    colnames.append(cat)
    this, that = ranges.split(' or ')
    tmp_ls += [i for i in range(int(this.split('-')[0]), int(this.split('-')[1])+1)]
    tmp_ls += [i for i in range(int(that.split('-')[0]), int(that.split('-')[1])+1)]
    for i in tmp_ls:
        if i in cat_dt:
            cat_dt[i].append(cat)
        else:
            cat_dt[i] = [cat]
    range_ls += tmp_ls


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
    bad_tickets = []
    for idx, ticket in enumerate(other_tickets):
        for num in ticket:
            if num not in range_ls:
                bad_tickets.append(idx)
                break
    valid_tickets = [i for idx, i in enumerate(other_tickets) if idx not in bad_tickets]
    return valid_tickets


def better_dt(cat_dt):
    best_dt = {}
    for cat_ls in cat_dt.values():
        for cat in cat_ls:
            for k, v in cat_dt.items():
                if cat not in v:
                    best_dt[k] = v
    return best_dt


def another(ticket, best_dt, df):
    for idx, val in enumerate(ticket):
        if val in best_dt:
            for cat in best_dt[val]:
                df[cat][idx] = df[cat][idx] + 1


def a_final(df, my_ticket):
    answer_ls = []

    for idx1, row in df.iterrows():
        the_max = max(list(row))
        for idx2, col in enumerate(df):
            if row[idx2] < the_max:
                df[col][idx1] = 0

    for col in df:
        the_max = max(list(df[col]))
        for idx, row in enumerate(list(df[col])):
            if row < the_max:
                df[col][idx] = 0
            elif col.startswith('departure'):
                answer_ls.append(my_ticket[idx])

    product = 1
    for i in answer_ls:
        product = product * i

    print(product)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        my_ticket, other_tickets, range_ls, cat_dt, df = ticket_info(f)
    for col in df:
        df[col] = [0 for i in range(len(my_ticket))]

    valid_tickets = test_tickets(my_ticket, other_tickets, range_ls)

    valid_tickets.append(my_ticket)

    best_dt = better_dt(cat_dt)

    for ticket in valid_tickets:
        another(ticket, best_dt, df)

    a_final(df, my_ticket)

    df.to_csv('test.csv')
