def get_reports():
    reports = []
    with open("Day2Nums.txt", "r") as f:
        while True:
            report = f.readline()
            if report == "":
                break
            report = report.split(" ")
            if report [-1][-1] == "\n":
                report[-1] = report[-1][:-1]
            report = [int(num) for num in report]
            reports.append(report)
    return reports

def check_safe(report):
    # If report is not increasing or decreasing
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return 0

    differences = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    for difference in differences:
        if difference < 1 or difference > 3:
            return 0
    return 1


def part1():
    reports = get_reports()

    count = 0
    for report in reports:
        count += check_safe(report)
    print(f"Part 1: {count}")

def part2():
    reports = get_reports()

    count = 0
    for report in reports:
        for i in range(len(report)):
            temp_report = report[:i] + report[i + 1:]
            if check_safe(temp_report):
                count += 1
                break
    print(f"Part 2: {count}")
part1()
part2()