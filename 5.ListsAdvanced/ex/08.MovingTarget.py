target = [int(x) for x in input().split(" ")]


def shoot(t, idx, p):
    if 0 <= idx < len(t):
        t[idx] -= p
        if t[idx] <= 0:
            t.remove(t[idx])
            return t
    return t


def add(t, idx, v):
    if 0 <= idx < len(t):
        t.insert(idx, v)
    else:
        print("Invalid placement!")
    return t


def strike(t, idx, r):
    left_index = idx - r
    right_index = idx + r
    if left_index >= 0 and right_index < len(t):
        left_part = t[:left_index]
        right_part = t[right_index + 1:]
        t = left_part + right_part
    else:
        print("Strike missed!")
    return t


command = input()
while command != "End":
    tokens = command.split(" ")
    action = tokens[0]
    index = int(tokens[1])
    if action == "Shoot":
        power = int(tokens[2])
        target = shoot(target, index, power)
    elif action == "Add":
        value = int(tokens[2])
        target = add(target, index, value)
    elif action == "Strike":
        radius = int(tokens[2])
        target = strike(target, index, radius)

    command = input()

print("|".join([str(el) for el in target]))
