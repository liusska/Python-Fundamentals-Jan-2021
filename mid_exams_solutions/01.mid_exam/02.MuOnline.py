rooms = input().split("|")

health = 100
bitcoins = 0
is_death = False
rooms_count = 0

for room in rooms:
    rooms_count += 1
    command, number = room.split()
    number = int(number)
    if command == "potion":
        if health < 100:
            if health + number < 100:
                health += number
                print(f"You healed for {number} hp.")
            else:
                new_health = 100 - health
                health = 100
                print(f"You healed for {new_health} hp.")
            print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms_count}")
            is_death = True
            break

if not is_death:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
