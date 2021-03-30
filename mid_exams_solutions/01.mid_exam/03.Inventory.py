items_list = input().split(", ")


def collect(data, list_for_change):
    if data not in list_for_change:
        list_for_change.append(data)
    return list_for_change


def remove_item(data, list_for_change):
    if data in list_for_change:
        list_for_change.remove(data)
    return list_for_change


def move_to_the_end(data, list_for_change):
    if data in list_for_change:
        list_for_change.remove(data)
        list_for_change.append(data)
    return list_for_change


def combine_items(old, new, list_for_change):
    if old in list_for_change:
        old_item_idx = list_for_change.index(old)
        list_for_change.insert(old_item_idx + 1, new)
    return list_for_change


while True:
    command = input()
    if command == "Craft!":
        break
    action, item = command.split(" - ")
    if action == "Collect":
        items_list = collect(item, items_list)
    elif action == "Drop":
        items_list = remove_item(item, items_list)
    elif action == "Renew":
        items_list = move_to_the_end(item, items_list)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        items_list = combine_items(old_item, new_item,items_list)


print(', '.join(items_list))