wagons = int(input())

train = [0] * wagons
command = input()

while command != "End":
    tokens = command.split(" ")
    action = tokens[0]
    if action == "add":
        people = int(tokens[1])
        train[wagons - 1] += people
    elif action == "insert":
        position = int(tokens[1])
        people = int(tokens[2])
        train[position] += people
    elif action == "leave":
        position = int(tokens[1])
        people = int(tokens[2])
        train[position] -= people
    command = input()

print(train)