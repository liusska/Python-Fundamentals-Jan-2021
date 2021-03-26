divisor = int(input())
bound = int(input())
max_multiple = 0

for n in range(1, bound + 1):
    if n % divisor == 0:
        if n > max_multiple:
            max_multiple = n

print(max_multiple)