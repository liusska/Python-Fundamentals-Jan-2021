def cast_spell(name, mp_needed, spell_name):
    hero = [h for h in heroes if h.name == name][0]
    if hero.mp >= mp_needed:
        hero.mp -= mp_needed
        print(f"{hero.name} has successfully cast {spell_name} and now has {hero.mp} MP!")
    else:
        print(f"{hero.name} does not have enough MP to cast {spell_name}!")


def take_damage(name, damage, attacker):
    hero = [h for h in heroes if h.name == name][0]
    hero.hp -= damage
    if hero.hp > 0:
        print(f"{hero.name} was hit for {damage} HP by {attacker} and now has {hero.hp} HP left!")
    else:
        heroes.remove(hero)
        print(f"{hero.name} has been killed by {attacker}!")


def recharge(name, amount):
    hero = [h for h in heroes if h.name == name][0]
    if hero.mp < Hero.MAX_MP:
        hero.mp += amount
        if hero.mp > Hero.MAX_MP:
            temp = hero.mp - Hero.MAX_MP
            diff = amount - temp
            amount = diff
            hero.mp = Hero.MAX_MP
        print(f"{hero.name} recharged for {amount} MP!")
    else:
        print(f"{hero.name} recharged for 0 MP!")


def heal(name, amount):
    hero = [h for h in heroes if h.name == name][0]
    if hero.hp < Hero.MAX_HP:
        hero.hp += amount
        if hero.hp > Hero.MAX_HP:
            temp = hero.hp - Hero.MAX_HP
            diff = amount - temp
            amount = diff
            hero.hp = Hero.MAX_HP
        print(f"{hero.name} healed for {amount} HP!")
    else:
        print(f"{hero.name} healed for 0 HP!")


class Hero:
    MAX_HP = 100
    MAX_MP = 200

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def __repr__(self):
        return f"{self.name}\n  HP: {self.hp}\n  MP: {self.mp}"


n = int(input())
heroes = []
for _ in range(n):
    current_hero = input().split()
    current_name = current_hero[0]
    current_hp = int(current_hero[1])
    current_mp = int(current_hero[2])
    hero = Hero(current_name, current_hp, current_mp)
    heroes.append(hero)

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

sorted_heroes = sorted(heroes, key=lambda h: (-h.hp, h.name))

for hero in sorted_heroes:
    print(hero)
