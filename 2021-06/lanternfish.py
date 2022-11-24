def get_fish():
    with open("Advent_of_Code-assignment/2021-06/lanternfish.txt", "rt") as f:
        return [int(entry) for entry in f.readline().split(",")]

def part_1(fishies):
    fish_timers = list(fishies)
    days = 80

    for _ in range(days):
        new_fish = []
        for fish in enumerate(fish_timers):
            fish_timers[fish[0]] -= 1
            if fish_timers[fish[0]] == -1:
                new_fish.append(8)
                fish_timers[fish[0]] = 6
        fish_timers.extend(new_fish)
    return len(fish_timers)

def part_2(fishies):
    fish_timers = list(fishies)

if __name__ == "__main__":
    fishies = get_fish()
    # print(part_1(fishies))
    print(part_2(fishies))
