def solver():
    with open("day2/input.txt") as f:
        content = f.read()
    reports = content.split("\n")
    reports = [[int(val) for val in report.split(" ")] for report in reports]
    valid_reports = [report for report in reports if check_safe_report(report)]
    invalid_reports = [report for report in reports if not check_safe_report(report)]
    one_removal_report = [
        report for report in invalid_reports if check_one_removal_report(report)
    ]
    # print(valid_reports)
    # print(one_removal_report)
    print(len(valid_reports) + len(one_removal_report))

def check_safe_report(report: list[int]):
    sorted_report = sorted(report)
    if sorted_report != report and sorted_report != report[::-1]:
        return False
    diffs = [
        sorted_report[i] - sorted_report[i - 1] for i in range(1, len(sorted_report))
    ]
    return all(diff > 0 and diff <= 3 for diff in diffs)

def check_one_removal_report(report: list[int]):
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1 :]
        if check_safe_report(new_report):
            return True
    return False
