lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
costs = 0
count = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        if i % 3 == 0:
            costs += shield_price
            count += 1
            if count % 2 == 0:
                costs += armour_price
        costs += helmet_price
    if i % 3 == 0:
        costs += sword_price

print(f"Gladiator expenses: {round(costs):.2f} aureus")