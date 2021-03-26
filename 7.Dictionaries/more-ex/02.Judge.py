users = {}
contests = {}

while True:
    command = input()
    if command == "no more time":
        break

    name, subject, points = command.split(" -> ")
    points = int(points)
    if subject not in contests:
        contests[subject] = {name: 0}
    if name not in contests[subject]:
        contests[subject][name] = 0
    if points > contests[subject][name]:
        contests[subject][name] = points

    if name not in users:
        users[name] = {subject:points}
    elif subject not in users[name]:
        users[name][subject] = points
    elif users[name][subject] < points:
        users[name][subject] = points

    if users[name][subject] < points:
        users[name][subject] = points


for keys, values in contests.items():
    i = 0
    print(f'{keys}: {len(values)} participants')
    sorted_contests = dict(sorted(values.items(), key=lambda x: (-x[1], x[0])))
    for key, value in sorted_contests.items():
        i += 1
        print(f"{i}. {key} <::> {value}")


print("Individual standings:")
sorted_users = dict(sorted(users.items(), key=lambda x: (-sum(x[1].values()),x[0])))
i = 0
for key, value in sorted_users.items():
    print(f"{i}. {key} -> {sum(value.values())}")