text = input().split(" ")
first_str = text[0]
second_str = text[1]

total_sum = 0
for i in range(max(len(first_str), len(second_str))):
    if i < len(first_str) and i < len(second_str):
        total_sum += ord(first_str[i]) * ord(second_str[i])
    else:
        if i < len(first_str):
            total_sum += ord(first_str[i])
        else:
            total_sum += ord(second_str[i])

print(total_sum)