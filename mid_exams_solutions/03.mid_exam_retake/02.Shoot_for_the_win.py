targets = [int(x) for x in input().split()]
shouts = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index in range(len(targets)) and targets[index] != -1:
        shouts += 1
        current_shout = targets[index]
        targets[index] = -1
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > current_shout:
                    targets[i] -= current_shout
                else:
                    targets[i] += current_shout

print(f"Shot targets: {shouts} -> {' '.join([str(x) for x in targets])}")
