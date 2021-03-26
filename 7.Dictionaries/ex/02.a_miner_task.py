miner = {}
while True:
    command = input()
    if command == "stop":
        break
    resource = command
    quantity = int(input())
    if resource not in miner:
        miner[resource] = 0
    miner[resource] += quantity

for key, value in miner.items():
    print(f"{key} -> {value}")