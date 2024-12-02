import pandas as pd
import numpy as np


def count_correct_reports(data: []) -> int:
    correct_reports = 0
    for report in data:
        diff = report.diff().dropna()
        if np.all(diff.between(1, 3)) or np.all(diff.between(-3, -1)):
            correct_reports += 1

    return correct_reports


def main():
    reports = []
    with open("puzzle_input.txt") as data_file:
        for report_str in data_file:
            reports.append(pd.Series(report_str.strip().split(" "), dtype=int))

    print(f"Number of correct reports: {count_correct_reports(reports)}")



if __name__ == '__main__':
    main()