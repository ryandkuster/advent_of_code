import pandas as pd
import sys


def find_2020_combos(exp_report):
    for i in exp_report['2020_minus_entry'].values:
        for j in exp_report['entry']:
            if i - j in exp_report['entry'].values:
                return (2020 - i) * (i - j) * j


if __name__ == '__main__':
    exp_report = pd.read_csv(sys.argv[1], header=None, names=['entry'])
    exp_report['2020_minus_entry'] = 2020 - exp_report['entry']
    print(find_2020_combos(exp_report))
