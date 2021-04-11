def plunder(city, people_to_kill, gold_to_steal):
    town = [t for t in towns if t.name == city][0]
    town.population -= people_to_kill
    town.gold -= gold_to_steal
    print(f"{city} plundered! {gold_to_steal} gold stolen, {people_to_kill} citizens killed.")
    if town.population <= 0 or town.gold <= 0:
        towns.remove(town)
        print(f"{city} has been wiped off the map!")


def prosper(city, gold_to_add):
    town = [t for t in towns if t.name == city][0]
    if gold_to_add < 0:
        print("Gold added cannot be a negative number!")
    else:
        town.gold += gold_to_add
        print(f"{gold_to_add} gold added to the city treasury. {city} now has {town.gold} gold.")


class Town:
    def __init__(self, name, population, gold):
        self.name = name
        self.population = population
        self.gold = gold

    def __repr__(self):
        return f"{self.name} -> Population: {self.population} citizens, Gold: {self.gold} kg"


towns = []
while True:
    command = input()
    if command == "Sail":
        break
    tokens = command.split("||")
    current_town = tokens[0]
    current_population = int(tokens[1])
    current_gold = int(tokens[2])

    if towns:
        existing_town = [t for t in towns if t.name == current_town]
        if existing_town:
            existing_town[0].population += current_population
            existing_town[0].gold += current_gold
            continue
    town = Town(current_town, current_population, current_gold)
    towns.append(town)

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("=>")
    if tokens[0] == "Plunder":
        plunder(tokens[1], int(tokens[2]), int(tokens[3]))
    elif tokens[0] == "Prosper":
        prosper(tokens[1], int(tokens[2]))

sorted_towns = sorted(towns, key=lambda t: (-t.gold, t.name))

if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town in sorted_towns:
        print(town)
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
