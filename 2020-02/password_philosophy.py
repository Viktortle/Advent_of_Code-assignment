def compile_list():
    with open("Advent_of_Code-assignment/2020-02/password_philosophy.txt", "rt") as f:
        return [entry for entry in f.readlines()]

all_passwords = compile_list()
possible_passwords = []

for i in range(len(all_passwords)):
    all_passwords[i] = all_passwords[i].split()

for i in range(len(all_passwords)):
    all_passwords[i][0] = all_passwords[i][0].split("-")
    all_passwords[i][1] = all_passwords[i][1][0]

for entry in all_passwords:
    if entry[2].count(entry[1]) in range(int(entry[0][0]), int(entry[0][1])+1):
        possible_passwords.append(entry)

print(len(possible_passwords))

possible_passwords = []

for entry in all_passwords:
    if entry[2][int(entry[0][0])-1] == entry[1][0]:
        if entry[2][int(entry[0][1])-1] != entry[1][0]:
            possible_passwords.append(entry)

    elif entry[2][int(entry[0][1])-1] == entry[1][0]:
        if entry[2][int(entry[0][0])-1] != entry[1][0]:
            possible_passwords.append(entry)

print(len(possible_passwords))