import re

pattern = r"(#|\|)(?P<name>[A-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9][0-9]{,3}|10000)\1"
data = input()

find_match = re.finditer(pattern, data)
total_calories = 0
food_info = []

for match in find_match:
    dict = match.groupdict()
    total_calories += int(dict['calories'])
    food_info.append(dict)

print(f"You have food to last you for: {total_calories // 2000} days!")
for food in food_info:
    print(f"Item: {food['name']}, Best before: {food['date']}, Nutrition: {food['calories']}")

