def take_odd_idx():
    data = [ch for ch in password]
    new_password = ""
    for i in range(len(data)):
        if not i % 2 == 0:
            new_password += data[i]
    print(new_password)
    return new_password


def cut(data, idx, length_to_cut):
    word_to_cut = data[idx: idx+length_to_cut]
    data = data.replace(word_to_cut, "", 1)
    print(data)
    return data


def replace(data, old_part, new_part):
    if old_part in data:
        data = data.replace(old_part, new_part)
        print(data)
    else:
        print("Nothing to replace!")
    return data


password = input()

while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {password}")
        break
    tokens = command.split()
    if tokens[0] == "TakeOdd":
        password = take_odd_idx()
    elif tokens[0] == "Cut":
        index = int(tokens[1])
        length = int(tokens[2])
        password = cut(password, index, length)
    elif tokens[0] == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]
        password = replace(password, substring, substitute)
