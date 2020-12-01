import pandas as pd
import sys


def main():
    exp_report = pd.read_csv(sys.argv[1], header=None, names=['entry'])
    exp_report['2020_minus_entry'] = 2020 - exp_report['entry']
    answer = find_2020_combos(exp_report)
    print(answer)


def find_2020_combos(exp_report):
    for i in exp_report['entry'].values:
        if i in exp_report['2020_minus_entry'].values:
            return ((2020 - i) * i)


if __name__ == '__main__':
    main()
