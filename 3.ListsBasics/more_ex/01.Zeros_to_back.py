numbers = [int(x) for x in input().split(", ")]

for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers.append(numbers[i])
        numbers.remove(numbers[i])

print(numbers)