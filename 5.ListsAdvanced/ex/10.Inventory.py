items = input().split(", ")


def collect(item_to_add):
    if item_to_add not in items:
        items.append(item_to_add)


def drop(item_to_drop):
    if item_to_drop in items:
        items.remove(item_to_drop)


def combine_item(old, new):
    if old in items:
        idx = 0
        for i in range(0, len(items) - 1):
            if items[i] == old:
                idx = i + 1
        items.insert(idx, new)


def renew(item_to_add):
    if item_to_add in items:
        items.remove(item_to_add)
        items.append(item_to_add)


command = input()

while command != "Craft!":
    tokens = command.split(" - ")
    action = tokens[0]
    if action == "Collect":
        item = tokens[1]
        collect(item)
    elif action == "Drop":
        item = tokens[1]
        drop(item)
    elif action == "Combine Items":
        charts = tokens[1].split(":")
        old_item = charts[0]
        new_item = charts[1]
        combine_item(old_item, new_item)
    elif action == "Renew":
        item = tokens[1]
        renew(item)
    command = input()

print(", ".join([item for item in items]))