text = [str(x) for x in input()]
numbers = [int(ch) for ch in text if ch.isdigit()]
characters = [ch for ch in text if not ch.isdigit()]
take_list = []
skip_list = []
message = []
for i in range(len(numbers)):
    if i % 2 == 0:
        take_list.append(numbers[i])
    else:
        skip_list.append(numbers[i])

for num in take_list:
    message += characters[:num]
    characters = characters[num:]
    skip = skip_list.pop(0)
    characters = characters[skip:]

print(''.join(message))