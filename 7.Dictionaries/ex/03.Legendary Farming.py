key_materials = {"fragments": 0, "motes": 0, "shards": 0}
junk = {}

while True:
    data = input().split()
    is_found = False
    for i in range(0, len(data), 2):
        item = (data[i+1]).lower()
        quantity = int(data[i])
        if item in key_materials:
            key_materials[item] += quantity
            if key_materials[item] >= 250:
                key_materials[item] -= 250
                if item == "shards":
                    print("Shadowmourne obtained!")
                elif item == "fragments":
                    print("Valanyr obtained!")
                elif item == "motes":
                    print("Dragonwrath obtained!")
                is_found = True
                break
        else:
            if item not in junk:
                junk[item] = 0
            junk[item] += quantity
        if is_found:
            break
    if is_found:
        break

sorted_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
sorted_junks = dict(sorted(junk.items(), key=lambda x: (x[0], x[1])))

for key, value in sorted_materials.items():
    print(f"{key}: {value}")

for key, value in sorted_junks.items():
    print(f"{key}: {value}")