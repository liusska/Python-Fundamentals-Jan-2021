n = int(input())
parking = {}

for _ in range(n):
    command = input().split()
    action = command[0]
    name = command[1]
    if action == "register":
        number = command[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {number}")
        else:
            parking[name] = number
            print(f"{name} registered {number} successfully")
    elif action == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking.pop(name)

for key, value in parking.items():
    print(f"{key} => {value}")