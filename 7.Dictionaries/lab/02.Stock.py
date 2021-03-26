data = input().split()
products = input().split()
stock_quantity = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i+1])
    if product not in stock_quantity:
        stock_quantity[product] = 0
    stock_quantity[product] = quantity

for product in products:
    if product not in stock_quantity:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {stock_quantity[product]} of {product} left")