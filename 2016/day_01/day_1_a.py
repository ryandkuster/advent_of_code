import sys


pos = (0, 0)
face = 'N'

turn_dt = {'N': [[(1, 0),'E'], [(-1, 0),'W']],
           'E': [[(0, -1),'S'], [(0, 1),'N']],
           'S': [[(-1, 0),'W'], [(1, 0),'E']],
           'W': [[(0, 1),'N'], [(0, -1),'S']]}

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        step_ls = f.readline().rstrip().split(', ')

    for step in step_ls:
        choice = 0 if step[0] == 'R' else 1
        turn, face = turn_dt[face][choice]
        pos = tuple(i+(j*int(step[1:])) for i, j in zip(pos, turn))

    print(abs(pos[0]) + abs(pos[1]))
