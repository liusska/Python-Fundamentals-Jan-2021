key = [int(x) for x in input().split()]

while True:
    i = 0
    message = ""
    line = input()
    if line == "find":
        break
    for ch in line:
        current = ord(ch) - key[i]
        message += chr(current)
        if i == len(key) - 1:
            i = 0
        else:
            i += 1

    idx_type = []
    for i in range(len(message)):
        if message[i] == "&":
            idx_type.append(int(i))
    type_treasure = message[idx_type[0]+1: idx_type[1]]

    start_coord_idx = message.index("<")
    end_coord_idx = message.index(">")
    coordinates_treasure = message[start_coord_idx+1:end_coord_idx]
    print(f"Found {type_treasure} at {coordinates_treasure}")
