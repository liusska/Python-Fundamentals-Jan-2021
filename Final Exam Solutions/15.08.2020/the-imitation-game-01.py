def move(data, count_letters):
    left_part = data[count_letters:]
    right_part = data[:count_letters]
    data = left_part + right_part
    return data


def insert_value(data, idx, value):
    left_part = data[:idx]
    right_part = data[idx:]
    data = left_part + value + right_part
    return data


def change(data, old_piece, new_piece):
    if old_piece in data:
        data = data.replace(old_piece, new_piece)
    return data


message = input()

while True:
    command = input()
    if command == "Decode":
        break
    tokens = command.split("|")
    if tokens[0] == "Move":
        number_of_letter = int(tokens[1])
        message = move(message, number_of_letter)
    elif tokens[0] == "Insert":
        index = int(tokens[1])
        substring = tokens[2]
        message = insert_value(message, index, substring)
    elif tokens[0] == "ChangeAll":
        substr = tokens[1]
        replacement = tokens[2]
        message = change(message, substr, replacement)

print(f"The decrypted message is: {message}")
