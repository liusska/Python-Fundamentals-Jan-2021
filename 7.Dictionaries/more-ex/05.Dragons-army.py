class Dragons:
    def __init__(self, name, damage, health, armor):
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor

    def __repr__(self):
        return f"-{self.name} -> damage: {self.damage}, health: {self.health}, armor: {self.armor}"


count = int(input())
dragons_type = {}

for _ in range(count):
    command = input().split()

    type = command[0]
    drag_name = command[1]
    drag_damage = command[2]
    if drag_damage == "null":
        drag_damage = 45
    drag_health = command[3]
    if drag_health == "null":
        drag_health = 250
    drag_armor = command[4]
    if drag_armor == "null":
        drag_armor = 10

    dragon = Dragons(drag_name, int(drag_damage), int(drag_health), int(drag_armor))
    if type not in dragons_type:
        dragons_type[type] = [dragon]
    else:
        dragon_before = [dr for dr in dragons_type[type] if dr.name == drag_name]
        if not dragon_before:
            dragons_type[type].append(dragon)
        else:
            dragons_type[type].remove(dragon_before[0])
            dragons_type[type].append(dragon)

for key, value in dragons_type.items():
    sorted_values = (sorted(value, key=lambda drag: drag.name))
    total_damage = 0
    total_health = 0
    total_armor = 0
    for dragon in sorted_values:
        total_damage += dragon.damage
        total_health += dragon.health
        total_armor += dragon.armor
    print(f"{key}::({total_damage / len(value):.2f}/{total_health / len(value):.2f}/{total_armor / len(value):.2f})")
    for dragon in sorted_values:
        print(dragon)


