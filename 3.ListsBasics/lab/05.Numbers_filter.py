n = int(input())
numbers = []
for i in range(0, n):
    num = int(input())
    numbers.append(num)

even = []
odd = []
negative = []
positive = []

command = input()
if command == "even":
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    print(even)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            odd.append(num)
    print(odd)
elif command == "negative":
    for num in numbers:
        if num < 0:
            negative.append(num)
    print(negative)
elif command == "positive":
    for num in numbers:
        if num >= 0:
            positive.append(num)
    print(positive)