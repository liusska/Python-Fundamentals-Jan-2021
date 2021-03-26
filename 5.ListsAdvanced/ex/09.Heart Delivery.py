houses = list(map(int, input().split("@")))

command = input()
current_index = 0

while command != "Love!":
    jump_length = int(command.split()[1])
    current_index += jump_length
    if current_index >= len(houses):
        current_index = 0
    if houses[current_index] != 0:
        houses[current_index] -= 2
        if houses[current_index] == 0:
            print(f"Place {current_index} has Valentine's day." )
    else:
        print(f"Place {current_index} already had Valentine's day.")
    command = input()

print(f"Cupid's last position was {current_index}.")
is_successful = True
for house in houses:
    if house != 0:
        is_successful = False
        break

count = 0
for house in houses:
    if house != 0:
        count += 1

if is_successful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")