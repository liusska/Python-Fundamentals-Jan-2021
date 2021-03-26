string = input().split(" ")
beggar = int(input())
numbers = []
for i in string:
    numbers.append(int(i))

for i in range(0, beggar):
    numbers.remove(min(numbers))

print(numbers)


