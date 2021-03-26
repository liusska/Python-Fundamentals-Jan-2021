line = input().split("|")
money = float(input())
purchases = []
buy_price = 0
cell_price = 0

for buy in line:
    product, price = buy.split("->")
    price = float(price)
    if product == "Clothes" and price <= 50:
        if money >= price:
            money -= price
            purchases.append(price * 1.40)
            cell_price += price * 1.40
            buy_price += price
    elif product == "Shoes" and price <= 35:
        if money >= price:
            money -= price
            purchases.append(price * 1.40)
            cell_price += price * 1.40
            buy_price += price
    elif product == "Accessories" and price <= 20.50:
        if money >= price:
            money -= price
            purchases.append(price * 1.40)
            cell_price += price * 1.40
            buy_price += price

for i in range(0, len(purchases)):
    if i == len(purchases) - 1:
        print(f"{purchases[i]:.2f}")
    else:
        print(f"{purchases[i]:.2f}", end=" ")

profit = cell_price - buy_price
print(f"Profit: {profit:.2f}")
total_money = money + cell_price
if total_money < 150:
    print("Time to go.")
else:
    print("Hello, France!")