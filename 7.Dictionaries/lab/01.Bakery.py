dict_data = input().split()
bakery_dict = {}

for i in range(0, len(dict_data), 2):
    if dict_data[i] not in bakery_dict:
        bakery_dict[dict_data[i]] = ""
    bakery_dict[dict_data[i]] = int(dict_data[i+1])

print(bakery_dict)