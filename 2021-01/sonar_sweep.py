counting = 0
result = 0

def measure():
    with open("Advent_of_Code-assignment/2021-01/sonar_sweep.txt", "rt") as f:
        return [int(entry) for entry in f.readlines()]

measurements = measure()

for i in measurements:
    if counting > 0:
        if i > measurements[counting-1]:
            result += 1
    counting += 1

print(result)

triplets = []

for i in range(len(measurements)-2):
    triplets.append(sum([measurements[i], measurements[i+1], measurements[i+2]]))

result_2 = 0
counting = 0

for i in triplets:
    if counting > 0:
        if i > triplets[counting-1]:
            result_2 += 1
    counting += 1

print(result_2)