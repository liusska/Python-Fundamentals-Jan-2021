def add_racer(racer, dist):
    if name not in racers:
        racers[racer] = 0
    racers[name] += dist


names = input().split(", ")
racers = {}

while True:
    command = input()
    if command == "end of race":
        break
    name = ""
    distance = 0
    for ch in command:
        if ch.isalpha():
            name += ch
        elif ch.isdigit():
            distance += int(ch)
    if name in names:
        add_racer(name, distance)

sorted_by_distance = sorted(racers.items(), key=lambda x: (-x[1]))
i = 0
idx = ""
for key, value in sorted_by_distance:
    i += 1
    if i == 1:
        idx = "1st"
    elif i == 2:
        idx = "2nd"
    elif i == 3:
        idx = "3rd"
    else:
        break
    print(f"{idx} place: {key}")