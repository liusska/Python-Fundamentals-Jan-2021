def add_user(user_to_add, side_to_join, force_dict):
    for s, u in force_dict.items():
        if user_to_add in u:
            return force_dict
    if side_to_join not in force_dict:
        force_dict[side_to_join] = []
        force_dict[side_to_join].append(user_to_add)
        return force_dict
    else:
        if user_to_add not in force_dict[side_to_join]:
            force_dict[side_to_join].append(name)
    return force_dict


def user_to_transfer(user, side_for_transfer, force_dict):
    for s, u in force_dict.items():
        if user in u:
            force_dict[s].remove(user)
            return add_user(user, side_for_transfer, force_dict)
    return add_user(user, side_for_transfer, force_dict)


force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        tokens = command.split(" | ")
        side, name = tokens[0], tokens[1]
        force_book = add_user(name, side, force_book)
    else:
        tokens = command.split(" -> ")
        name, side = tokens[0], tokens[1]
        force_book = user_to_transfer(name, side, force_book)
        print(f"{name} joins the {side} side!")


sorted_force = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))


for key, value in sorted_force.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for val in sorted(value):
            print(f"! {val}")
