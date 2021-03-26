first = input().split(", ")
second = input().split(", ")

substring_list = []

for f in first:
    for s in second:
        if f in s and f not in substring_list:
            substring_list.append(f)

print(substring_list)