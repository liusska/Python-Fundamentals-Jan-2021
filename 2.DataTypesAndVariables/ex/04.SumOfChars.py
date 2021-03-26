n = int(input())

total_sum = 0

for i in range(0, n):
    ch = input()
    total_sum += ord(ch)

print(f"The sum equals: {total_sum}")