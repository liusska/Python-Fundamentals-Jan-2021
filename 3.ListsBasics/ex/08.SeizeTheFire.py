line = input().split("#")
water = int(input())
fire_burn = []
total_fire_effort = 0
total_fire = 0
for fire in line:
    tokens = fire.split(" = ")
    level = tokens[0]
    value = int(tokens[1])
    if level == "High":
        if 81 <= value <= 125:
            if water >= value:
                water -= value
                fire_burn.append(value)
        else:
            continue
    elif level == "Medium":
        if 51 <= value <= 80:
            if water >= value:
                water -= value
                fire_burn.append(value)
        else:
            continue
    elif level == "Low":
        if 1 <= value <= 50:
            if water >= value:
                water -= value
                fire_burn.append(value)
        else:
            continue

print("Cells:")
for fire in fire_burn:
    total_fire_effort += fire * 0.25
    total_fire += fire
    print(f" - {fire}")

print(f"Effort: {total_fire_effort:.2f}")
print(f"Total Fire: {total_fire}")