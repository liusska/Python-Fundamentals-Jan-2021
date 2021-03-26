product = input()
count = int(input())


def total_price(name, quantity):
    total = 0
    if name == "coffee":
        total = quantity * 1.50
    elif name == "water":
        total = quantity * 1
    elif name == "coke":
        total = quantity * 1.40
    elif name == "snacks":
        total = quantity * 2
    return total


print(f"{total_price(product, count):.2f}")