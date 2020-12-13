import sys



turn_dt = {'N': [[(1, 0),'E'], [(-1, 0),'W']],
           'E': [[(0, -1),'S'], [(0, 1),'N']],
           'S': [[(-1, 0),'W'], [(1, 0),'E']],
           'W': [[(0, 1),'N'], [(0, -1),'S']]}

def path_maker(step_ls):
    pos = (0, 0)
    steps_taken = [pos]
    face = 'N'
    for step in step_ls:
        choice = 0 if step[0] == 'R' else 1
        turn, face = turn_dt[face][choice]
        for i in range(int(step[1:])):
            pos = tuple(i+j for i, j in zip(pos, turn))
            steps_taken.append(pos)
            if steps_taken.count(pos) > 1:
                return pos


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        step_ls = f.readline().rstrip().split(', ')

    pos = path_maker(step_ls)

    print(abs(pos[0]) + abs(pos[1]))
