def add_rate(list_of_obj, name, rating):
    plant = [obj for obj in list_of_obj if obj.name == name]
    if not plant:
        print("error")
    else:
        plant[0].ratings.append(rating)
    return list_of_obj


def update_rarity(list_of_obj, name, rarity):
    plant = [obj for obj in list_of_obj if obj.name == name]
    if not plant:
        print("error")
    else:
        plant[0].rarity = rarity
    return list_of_obj


def reset_rate(list_of_obj, name):
    plant = [obj for obj in list_of_obj if obj.name == name]
    if not plant:
        print("error")
    else:
        plant[0].ratings.clear()
    return list_of_obj


class Plant:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.ratings = []

    def rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0

    def __repr__(self):
        return f"- {self.name}; Rarity: {self.rarity}; Rating: {self.rating():.2f}"


n = int(input())
plants = []
for _ in range(n):
    current_name, current_rarity = input().split("<->")
    current_plant = Plant(current_name, int(current_rarity))
    plants.append(current_plant)

while True:
    command = input()
    if command == "Exhibition":
        break
    tokens = command.split(": ")
    if tokens[0] == "Rate":
        items = tokens[1].split(" - ")
        plant_name = items[0]
        new_rating = int(items[1])
        plants = add_rate(plants, plant_name, new_rating)

    elif tokens[0] == "Update":
        items = tokens[1].split(" - ")
        plant_name = items[0]
        new_rarity = int(items[1])
        plants = update_rarity(plants, plant_name, new_rarity)

    elif tokens[0] == "Reset":
        plant_name = tokens[1]
        plants = reset_rate(plants, plant_name)
    else:
        print("error")

print("Plants for the exhibition:")
sorted_plants = sorted(plants, key=lambda x: (x.rarity, x.rating()), reverse=True)

for pl in sorted_plants:
    print(pl)
