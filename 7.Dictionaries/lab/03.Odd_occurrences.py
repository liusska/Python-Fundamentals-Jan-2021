data = input().split()

occurrences = {}

for i in range(len(data)):
    element = data[i].lower()
    if element not in occurrences:
        occurrences[element] = 0
    occurrences[element] += 1

for key, val in occurrences.items():
    if not val % 2 == 0:
        print(key, end=" ")
