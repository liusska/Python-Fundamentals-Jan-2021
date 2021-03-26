import re

data = input()
pattern = r"(=|/){1}(?P<destination>[A-Z][A-Za-z]{2,})\1"
find_destination = re.finditer(pattern, data)
travel_points = 0

destinations = []
for match in find_destination:
    obj_dict = match.groupdict()
    destinations.append(obj_dict)

dest_list_for_preview = []
for dest in destinations:
    for key, values in dest.items():
        dest_list_for_preview.append(values)
        travel_points += len(values)

print(f"Destinations: {', '.join(dest_list_for_preview)}")
print(f"Travel Points: {travel_points}")

