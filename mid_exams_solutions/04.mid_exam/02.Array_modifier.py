data = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break
    action = command.split()[0]
    if action == "swap":
        idx1 = int(command.split()[1])
        idx2 = int(command.split()[2])
        data[idx1], data[idx2] = data[idx2], data[idx1]
    elif action == "multiply":
        idx1 = int(command.split()[1])
        idx2 = int(command.split()[2])
        data[idx1] *= data[idx2]
    elif action == "decrease":
        for i in range(len(data)):
            data[i] -= 1

print(', '.join([str(x) for x in data]))