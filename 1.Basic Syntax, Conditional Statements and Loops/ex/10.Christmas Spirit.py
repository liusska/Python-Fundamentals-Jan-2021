quantity = int(input())
days = int(input())
spirit = 0
cost = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        cost += ornament_set_price * quantity
        spirit += 5
    if i % 3 == 0:
        cost += (tree_skirt_price + tree_garlands_price) * quantity
        spirit += 13
    if i % 5 == 0:
        cost += tree_lights_price * quantity
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        cost += tree_skirt_price + tree_garlands_price + tree_lights_price


if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")