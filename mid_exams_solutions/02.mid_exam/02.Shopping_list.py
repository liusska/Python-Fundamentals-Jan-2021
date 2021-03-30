products_list = input().split("!")


def add_item(item, products):
    if item not in products:
        products.insert(0, item)
    return products


def remove_item(item, products):
    if item in products:
        products.remove(item)
    return products


def rearrange(item, products):
    if item in products:
        products.remove(item)
        products.append(item)
    return products


def correct_list(old, new, products):
    if old in products:
        idx = products.index(old)
        products.remove(old)
        products.insert(idx, new)
    return products


while True:
    command = input()
    if command == "Go Shopping!":
        break
    action = command.split()[0]
    if action == "Urgent":
        products_list = add_item(command.split()[1], products_list)
    elif action == "Unnecessary":
        products_list = remove_item(command.split()[1], products_list)
    elif action == "Correct":
        products_list = correct_list(command.split()[1], command.split()[2], products_list)
    elif action == "Rearrange":
        products_list = rearrange(command.split()[1], products_list)


print(', '.join(products_list))