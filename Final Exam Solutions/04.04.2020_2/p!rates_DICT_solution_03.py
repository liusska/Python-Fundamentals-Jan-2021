def add_gold(town, gold_for_increase, gold_dict):
    if gold_for_increase < 0:
        print("Gold added cannot be a negative number!" )
    else:
        gold_dict[town] += gold_for_increase
        print(f"{gold_for_increase} gold added to the city treasury. {town} now has {gold_dict[town]} gold.")


def attack_city(killed_people, stolen_gold, city, population, gold):
    population[city] -= killed_people
    gold[city] -= stolen_gold
    print(f"{city} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.")
    if population[city] <= 0 or gold[city] <= 0:
        print(f"{city} has been wiped off the map!")
        del population[city]
        del gold[city]


cities_population = {}
cities_gold = {}


while True:
    command = input()
    if command == "Sail":
        break
    tokens = command.split("||")
    city = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])
    if city not in cities_population:
        cities_population[city] = 0
        cities_gold[city] = 0
    cities_population[city] += population
    cities_gold[city] += gold


while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("=>")
    if tokens[0] == "Plunder":
        attack_city(int(tokens[2]), int(tokens[3]), tokens[1], cities_population, cities_gold)
    elif tokens[0] == "Prosper":
        add_gold(tokens[1], int(tokens[2]), cities_gold)

print(f"Ahoy, Captain! There are {len(cities_population)} wealthy settlements to go to:")
if len(cities_gold) > 0:
    sorted_cities = sorted(cities_gold.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_cities:
        print(f"{key} -> Population: {cities_population[key]} citizens, Gold: {value} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")