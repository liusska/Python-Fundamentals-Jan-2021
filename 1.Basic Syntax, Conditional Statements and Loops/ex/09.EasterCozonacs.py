budget = float(input())
flour_price_per_kg = float(input())

colored_eggs = 0
cozonac_count = 0

eggs_price_per_pack = flour_price_per_kg * 0.75
milg_per_one_liter = flour_price_per_kg * 1.25
milk_per_one_cozonac = milg_per_one_liter * 0.25
one_cozonac_total_price = eggs_price_per_pack + milk_per_one_cozonac + flour_price_per_kg

while budget >= one_cozonac_total_price:
    cozonac_count += 1
    colored_eggs += 3
    budget -= one_cozonac_total_price
    if cozonac_count % 3 == 0:
        colored_eggs -= cozonac_count - 2

print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")