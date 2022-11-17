def compile_list():
    with open("Advent_of_Code-assignment/2019-01/rocket_equation.txt", "rt") as f:
        return [int(entry) for entry in f.readlines()]

def calc_fuel(weight):
    fuel = (weight//3)-2
    if fuel <= 0: 
        return 0
    else: 
        return fuel + calc_fuel(fuel)

module_weights = compile_list()
total_fuel = 0

for entry in module_weights:
    total_fuel += calc_fuel(entry)
else: print(total_fuel)