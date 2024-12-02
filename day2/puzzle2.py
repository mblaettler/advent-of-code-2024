import pandas as pd


def count_correct_reports(data: []) -> int:
    correct_reports = 0
    for report in data:
        diff = report.diff()
        if diff.max() <= 3 and diff.min() > 0:
            correct_reports += 1
        elif diff.min() >= -3 and diff.max() < 0:
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