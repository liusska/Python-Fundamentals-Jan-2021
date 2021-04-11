def insert_space(data, idx):
    left_part = data[:idx]
    right_part = data[idx:]
    data = left_part + " " + right_part
    print(data)
    return data


def reverse_part(data, substring):
    if substring in data:
        data = data.replace(substring, "", 1)
        reversed_part = substring[::-1]
        data += reversed_part
        print(data)
    else:
        print("error")
    return data


def change_all(data, old_part, new_part):
    if old_part in data:
        data = data.replace(old_part, new_part)
        print(data)
    return data


message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    tokens = command.split(":|:")
    if tokens[0] == "InsertSpace":
        message = insert_space(message, int(tokens[1]))
    elif tokens[0] == "Reverse":
        message = reverse_part(message, tokens[1])
    elif tokens[0] == "ChangeAll":
        message = change_all(message, tokens[1], tokens[2])

print(f"You have a new text message: {message}")