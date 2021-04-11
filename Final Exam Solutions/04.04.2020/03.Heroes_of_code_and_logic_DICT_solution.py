def add_heroes(name, hit_points, mana_points):
    if name not in heroes_hp:
        heroes_hp[name] = 0
        heroes_mp[name] = 0
    heroes_hp[name] += hit_points
    heroes_mp[name] += mana_points
    if heroes_hp[name] > 100:
        heroes_hp[name] = 100
    if heroes_mp[name] > 200:
        heroes_mp[name] = 200


def cast_spell(name, mp_needed, spell):
    if heroes_mp[name] >= mp_needed:
        heroes_mp[name] -= mp_needed
        print(f"{name} has successfully cast {spell} and now has {heroes_mp[name]} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")


def take_damage(name, damage, attacker):
    heroes_hp[name] -= damage
    if heroes_hp[name] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_hp[name]} HP left!")
    else:
        print(f"{name} has been killed by {attacker}!")
        del heroes_hp[name]
        del heroes_mp[name]


def recharge(name, amount):
    heroes_mp[name] += amount
    if heroes_mp[name] > 200:
        diff = heroes_mp[name] - 200
        total_diff = amount - diff
        heroes_mp[name] = 200
        print(f"{name} recharged for {total_diff} MP!")
    else:
        print(f"{name} recharged for {amount} MP!")


def heal(name, amount):
    heroes_hp[name] += amount
    if heroes_hp[name] > 100:
        diff = heroes_hp[name] - 100
        total_diff = amount - diff
        heroes_hp[name] = 100
        print(f"{name} healed for {total_diff} HP!")
    else:
        print(f"{name} healed for {amount} HP!")


heroes_hp = {}
heroes_mp = {}
heroes_count = int(input())

for _ in range(heroes_count):
    hero, hp, mp = input().split(" ")
    add_heroes(hero, int(hp), int(mp))

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split(" - ")
    if tokens[0] == "CastSpell":
        cast_spell(tokens[1], int(tokens[2]), tokens[3])
    elif tokens[0] == "TakeDamage":
        take_damage(tokens[1], int(tokens[2]), tokens[3])
    elif tokens[0] == "Recharge":
        recharge(tokens[1], int(tokens[2]))
    elif tokens[0] == "Heal":
        heal(tokens[1], int(tokens[2]))


sorted_by_hp = sorted(heroes_hp.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_by_hp:
    print(f"{key}")
    print(f"  HP: {value}")
    print(f"  MP: {heroes_mp[key]}")