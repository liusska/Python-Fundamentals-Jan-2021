numbers = [int(x) for x in input().split()]

average_num = sum(numbers) / len(numbers)

numbers = [num for num in numbers if num > average_num]
sorted_numbers = sorted(numbers, reverse=True)

if sorted_numbers:
    print(' '. join(str(x) for x in sorted_numbers[:5]))
else:
    print("No")