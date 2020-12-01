import pandas as pd
import sys


def main():
    exp_report = pd.read_csv(sys.argv[1], header=None, names=['entry'])
    exp_report['2020_minus_entry'] = 2020 - exp_report['entry']
    answer = find_2020_combos_3(exp_report)
    print(answer)


def find_2020_combos_3(exp_report):
    for i in exp_report['2020_minus_entry'].values:
        for j in exp_report['entry']:
            if i - j in exp_report['entry'].values:
                print(str(2020 - i), str(i - j), j)
                return (2020 - i) * (i - j) * j


if __name__ == '__main__':
    main()
