prices = {}
quantities = {}
while True:
    command = input()
    if command == "buy":
        break
    tokens = command.split()
    product = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])
    if product not in prices:
        prices[product] = 0
    prices[product] = price
    if product not in quantities:
        quantities[product] = 0
    quantities[product] += quantity

for key, value in quantities.items():
    for k, v in prices.items():
        if key == k:
            total = v * value
            print(f"{key} -> {total:.2f}")
    total = 1
