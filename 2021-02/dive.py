def instructions():
    with open("Advent_of_Code-assignment/2021-02/dive.txt", "rt") as f:
        return [entry.split(" ") for entry in f.readlines()]

instructions_list = instructions()
depth = 0
distance = 0
aim = 0

for instruction in instructions_list:
    if instruction[0] == "forward":
        distance += int(instruction[1])
        depth += aim*int(instruction[1])
    elif instruction[0] == "down":
        aim += int(instruction[1])
    elif instruction[0] == "up":
        aim -= int(instruction[1])
else:
    print(depth*distance)