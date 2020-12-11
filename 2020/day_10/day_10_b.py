import copy
import sys


def count_jumps(jolt_ls):
    step_dt = {}
    for idx, i in enumerate(jolt_ls):
        step_dt[i] = []
        for j in jolt_ls[idx+1:]:
            if j - i < 4:
                step_dt[i].append(j)
    return step_dt


def count_trees(jolt_ls, step_dt):
    tree_dt = {0: 1}
    max_steps = max(step_dt.keys())
    total_count = 0
    counter = 0
    while counter <= max_steps:
        new_tree_dt = {}
        counter += 1
        for step, count in tree_dt.items():
            for next_step in step_dt[step]:
                if next_step in new_tree_dt:
                    new_tree_dt[next_step] += count
                else:
                    new_tree_dt[next_step] = count
        if max_steps in new_tree_dt:
            total_count += new_tree_dt[max_steps]
        tree_dt = new_tree_dt
    print(total_count)

if __name__ == '__main__':
    jolt_ls = [0]
    with open(sys.argv[1]) as f:
        jolt_ls += [int(i.rstrip()) for i in f]
    jolt_ls.sort()
    jolt_ls.append(max(jolt_ls) + 3)
    step_dt = count_jumps(jolt_ls)
    count_trees(jolt_ls, step_dt)
