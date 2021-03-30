prices = 0
taxes = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        prices += price
        taxes += price* 0.2

prices_with_taxes = prices + taxes

if command == "special":
    prices_with_taxes *= 0.90

if prices_with_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {prices:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {prices_with_taxes:.2f}$")