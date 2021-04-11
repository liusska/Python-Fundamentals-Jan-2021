def check_for_substring(word):
    if word in activation_key:
        print(f"{activation_key} contains {word}")
    else:
        print("Substring not found!")


def flip(data, case, start_idx, end_idx):
    change_case = data[start_idx:end_idx]
    left_part = data[:start_idx]
    right_part = data[end_idx:]
    if case == "Upper":
        data = left_part + change_case.upper() + right_part
    elif case == "Lower":
        data = left_part + change_case.lower() + right_part
    print(data)
    return data


def slice(data, start_idx, end_idx):
    left_part = data[:start_idx]
    right_part = data[end_idx:]
    data = left_part + right_part
    print(data)
    return data


activation_key = input()

while True:
    command = input()
    if command == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    tokens = command.split(">>>")
    if tokens[0] == "Contains":
        check_for_substring(tokens[1])
    elif tokens[0] == "Flip":
        activation_key = flip(activation_key, tokens[1], int(tokens[2]), int(tokens[3]))
    elif tokens[0] == "Slice":
        activation_key = slice(activation_key, int(tokens[1]), int(tokens[2]))