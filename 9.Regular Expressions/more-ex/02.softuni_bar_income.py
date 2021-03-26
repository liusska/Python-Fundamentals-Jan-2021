import re
pattern = r'\%([A-Z][a-z]+)\%[^|$%.]*\<(\w+)\>[^|$%.]*\|(\d+)\|[^|$%.]*?(\d+([.]\d+)?)\$'
total_order = 0
while True:
    command = input()
    if command == "end of shift":
        break
    current_order = re.findall(pattern, command)
    if current_order:
        for order in current_order:
            name = order[0]
            product = order[1]
            count = int(order[2])
            price = float(order[3])
            total_price = count * price
            print(f"{name}: {product} - {total_price:.2f}")
            total_order += total_price

print(f"Total income: {total_order:.2f}")