def compile_report():
    with open("Advent_of_Code-assignment/2020-01/report_repair.txt", "rt") as f:
        return [int(entry) for entry in f.readlines()]

report = compile_report()

for entry in report:
    for comparison in report:
        if entry + comparison == 2020:
            print(entry*comparison)

for entry in report:
    for comparison in report:
        for item in report:
            if entry + comparison + item == 2020:
                print(entry*comparison*item)