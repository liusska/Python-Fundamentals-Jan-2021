gifts = input().split(" ")

command = input()

while command != "No Money":
    tokens = command.split(" ")
    do = tokens[0]
    if do == "OutOfStock":
        gift = tokens[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"
    if do == "Required":
        gift = tokens[1]
        index = int(tokens[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    if do == "JustInCase":
        gift = tokens[1]
        gifts[-1] = gift

    command = input()

result = []
for gift in gifts:
    if gift != "None":
        result.append(gift)
print(" ".join(result))