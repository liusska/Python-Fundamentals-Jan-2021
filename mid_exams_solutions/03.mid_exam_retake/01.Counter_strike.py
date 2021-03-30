energy = int(input())
won_battles = 0
not_enough_energy = False
while True:
    command = input()
    if command == "End of battle":
        break
    distance = int(command)
    if energy - distance < 0:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        not_enough_energy = True
        break
    energy -= distance
    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles

if not not_enough_energy:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
