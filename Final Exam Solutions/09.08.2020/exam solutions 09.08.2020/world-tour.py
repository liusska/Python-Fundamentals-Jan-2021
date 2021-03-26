def add_string(data_for_change, idx, string_to_add):
    if idx in range(len(data_for_change)):
        data_for_change = data_for_change[:idx] + string_to_add + data_for_change[idx:]
    print(data_for_change)
    return data_for_change


def remove_stop(data_for_change, start_idx, end_idx):
    if start_idx in range(len(data_for_change)) and end_idx in range(len(data_for_change)):
        data_for_change = data_for_change[:start_idx] + data_for_change[end_idx+1:]
    print(data_for_change)
    return data_for_change


def replace_part(data_for_change, old_str, new_str):
    if old_str in data_for_change:
        data_for_change = data_for_change.replace(old_str, new_str)
    print(data_for_change)
    return data_for_change


travel_info = input()

while True:
    command = input()
    if command == "Travel":
        break
    tokens = command.split(":")
    if tokens[0] == "Add Stop":
        travel_info = add_string(travel_info, int(tokens[1]), tokens[2])
    elif tokens[0] == "Remove Stop":
        travel_info = remove_stop(travel_info, int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "Switch":
        travel_info = replace_part(travel_info, tokens[1], tokens[2])


print(f"Ready for world tour! Planned stops: {travel_info}")