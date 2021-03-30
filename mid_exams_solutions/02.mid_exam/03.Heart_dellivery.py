neighborhood = [int(x) for x in input().split("@")]
current_jump_idx = 0

while True:
    command = input()
    if command == "Love!":
        break
    jump = int(command.split()[1])
    current_jump_idx += jump
    if current_jump_idx >= len(neighborhood):
        current_jump_idx = 0
    if neighborhood[current_jump_idx] > 0:
        neighborhood[current_jump_idx] -= 2
        if neighborhood[current_jump_idx] == 0:
            print(f"Place {current_jump_idx} has Valentine's day.")
    elif neighborhood[current_jump_idx] == 0:
        print(f"Place {current_jump_idx} already had Valentine's day.")


print(f"Cupid's last position was {current_jump_idx}.")
house_without_valentine = 0
for house in neighborhood:
    if house > 0:
        house_without_valentine += 1

if house_without_valentine:
    print(f"Cupid has failed {house_without_valentine} places.")
else:
    print("Mission was successful.")