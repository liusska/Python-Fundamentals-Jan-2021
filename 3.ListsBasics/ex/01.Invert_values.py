inputs = input()
numbers = inputs.split(" ")
invert_numbers = []
for num in numbers:
    num = int(num)
    if num == 0:
        invert_numbers.append(num)
    elif num > 0:
        num = -1 * num
        invert_numbers.append(num)
    else:
        invert_numbers.append(abs(num))

print(invert_numbers)