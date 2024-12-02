def solver():
    with open("day2/input.txt") as f:
        content = f.read()
    reports = content.split("\n")
    reports = [[int(val) for val in report.split(" ")] for report in reports]
    valid_reports = [report for report in reports if check_safe_report(report)]
    print(len(valid_reports))

def check_safe_report(report: list[int]):
    sorted_report = sorted(report)
    if sorted_report != report and sorted_report != report[::-1]:
        return False
    diffs = [
        sorted_report[i] - sorted_report[i - 1] for i in range(1, len(sorted_report))
    ]
    return all(diff > 0 and diff <= 3 for diff in diffs)
