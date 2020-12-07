import re
import sys


def baggage_claim(f):
    bag_dt = {}
    bag_ls = []
    for rule in f:
        rule = rule.strip('.\n')
        inner, outer = bag_handler(rule, bag_dt)
        bag_dt = bag_dt_init(outer, inner, bag_dt)
    bag_ls = bag_dt_search(bag_dt, ['shiny gold'], bag_ls)
    print(len(bag_ls))


def bag_handler(rule, bag_dt):
    rule = re.sub(r'( bags| bag)', '', rule)
    outer, inner = rule.split(' contain ')
    inner = inner.split(', ')
    return inner, outer


def bag_dt_init(outer, inner, bag_dt):
    bag_dt[outer] = [bag for bag in inner]
    return bag_dt


def bag_dt_search(bag_dt, target_ls, bag_ls):
    new_target_ls = []
    for target in target_ls:
        for val in bag_dt[target]:
            try:
                num = int(re.findall(r'[0-9]+', val)[0])
                color = ' '.join(val.split(' ')[1:])
                this_turn = [color for i in range(num)]
            except IndexError:
                continue
            new_target_ls = new_target_ls + this_turn
            bag_ls = bag_ls + this_turn
    if len(new_target_ls) > 0:
        return bag_dt_search(bag_dt, new_target_ls, bag_ls)
    else:
        return bag_ls


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        baggage_claim(f)
