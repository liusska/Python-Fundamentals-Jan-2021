targets = [int(x) for x in input().split()]


def shout(idx, power, data):
    if idx in range(len(data)):
        data[idx] -= power
        if data[idx] <= 0:
            data.pop(idx)
    return data


def add(idx, power, data):
    if idx in range(len(data)):
        data.insert(idx, power)
    else:
        print("Invalid placement!")


def strike(idx, radius, data):
    if idx in range(len(data)):
        left_radius = idx - radius
        right_radius = idx + radius
        if left_radius in range(len(data)) and right_radius in range(len(data)):
            left_part = data[:left_radius]
            right_part = data[right_radius + 1:]
            data = left_part + right_part
        else:
            print("Strike missed!")
    return data


while True:
    command = input()
    if command == "End":
        break
    action, index, value = command.split()
    index = int(index)
    value = int(value)
    if action == "Shoot":
        targets = shout(index, value, targets)
    elif action == "Add":
        add(index, value, targets)
    elif action == "Strike":
        targets = strike(index, value, targets)

print('|'.join([str(x) for x in targets]))