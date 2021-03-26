working_events = input().split("|")

initial_energy = 100
initial_coins = 100
bankrupt = False

for event in working_events:
    tokens = event.split("-")
    command = tokens[0]

    if command == "rest":
        energy = int(tokens[1])
        if initial_energy + energy <= 100:
            initial_energy += energy
            print(f"You gained {energy} energy.")
        else:
            print("You gained 0 energy.")
        print(f"Current energy: {initial_energy}.")
    elif command == "order":
        money = int(tokens[1])
        if initial_energy - 30 >= 0:
            initial_coins += money
            initial_energy -= 30
            print(f"You earned {money} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        money = int(tokens[1])
        if initial_coins - money > 0:
            initial_coins -= money
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            bankrupt = True
            break

if not bankrupt:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")