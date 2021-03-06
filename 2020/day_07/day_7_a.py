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
    #print(len(set(bag_ls)))
    print(len(set(bag_ls)))


def bag_handler(rule, bag_dt):
    rule = re.sub(r'( bags| bag)', '', rule)
    outer, inner = rule.split(' contain ')
    inner = re.sub(r'\d ', '', inner)
    inner = inner.split(', ')
    return inner, outer


def bag_dt_init(outer, inner, bag_dt):
    bag_dt[outer] = {bag: None for bag in inner}
    return bag_dt


def bag_dt_search(bag_dt, target_ls, bag_ls):
    new_target_ls = []
    for target in target_ls:
        for k1, v1 in bag_dt.items():
            for k2, v2 in v1.items():
                if target in k2:
                    bag_ls.append(k1)
                    new_target_ls.append(k1)
    if len(new_target_ls) > 0:
        #print(new_target_ls)
        return bag_dt_search(bag_dt, new_target_ls, bag_ls)
    else:
        return bag_ls


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        baggage_claim(f)
