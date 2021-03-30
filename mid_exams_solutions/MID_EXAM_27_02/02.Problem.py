sugar_cubes = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "Mort":
        break
    tokens = command.split()
    if tokens[0] == "Add":
        sugar_cubes.append(int(tokens[1]))
    elif tokens[0] == "Remove":
        sugar_cubes.remove(int(tokens[1]))
    elif tokens[0] == "Replace":
        for i in range(len(sugar_cubes)):
            if sugar_cubes[i] == int(tokens[1]):
                sugar_cubes[i] = int(tokens[2])
                break
    elif tokens[0] == "Collapse":
        value = int(tokens[1])
        sugar_cubes = [el for el in sugar_cubes if el >= value]

print(' '.join([str(x) for x in sugar_cubes]))