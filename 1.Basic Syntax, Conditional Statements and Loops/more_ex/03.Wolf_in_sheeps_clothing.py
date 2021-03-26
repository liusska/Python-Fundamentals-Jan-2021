animals = input().split(", ")
sheep_in_danger = []
count = 0
for i in range(0, len(animals) - 1):
    if animals[i] == "wolf":
        sheep_in_danger = animals[i+1:]
        count = len(sheep_in_danger)

if count == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {count}! You are about to be eaten by a wolf!")