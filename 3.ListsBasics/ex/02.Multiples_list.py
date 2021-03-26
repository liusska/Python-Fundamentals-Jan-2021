factor = int(input())
count = int(input())
numbers = []
for i in range(1, count + 1):
    num = i * factor
    numbers.append(num)

print(numbers)