products_in_stock = {}

while True:
    command = input()
    if command == "statistics":
        break
    product = command.split(": ")[0]
    quantity = int(command.split(": ")[1])
    if product not in products_in_stock:
        products_in_stock[product] = 0
    products_in_stock[product] += quantity

print("Products in stock:")
total_quantities = 0
for key, value in products_in_stock.items():
    print(f"- {key}: {value}")
    total_quantities += value
print(f"Total Products: {len(products_in_stock)}")
print(f"Total Quantity: {total_quantities}")