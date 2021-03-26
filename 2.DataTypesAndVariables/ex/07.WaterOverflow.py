n = int(input())
capacity = 255
tank = 0

for i in range(0, n):
    current_water = int(input())
    if current_water + tank <= capacity:
        tank += current_water
    else:
        print("Insufficient capacity!")


print(tank)