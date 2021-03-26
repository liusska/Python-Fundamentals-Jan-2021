number_as_str = input()

number_list = []

for n in number_as_str:
    n = int(n)
    number_list.append(n)

sorted_number_as_str = sorted(number_list, reverse=True)

print(''.join(str(num) for num in sorted_number_as_str))