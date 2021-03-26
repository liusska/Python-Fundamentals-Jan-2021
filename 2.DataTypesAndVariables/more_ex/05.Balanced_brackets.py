n = int(input())

is_open = False
balanced = True

for i in range(n):
    line = input()
    if line == "(":
        if not is_open:
            is_open = True
        else:
            balanced = False
    elif line == ")":
        if is_open:
            is_open = False
        else:
            balanced = False

if balanced and not is_open:
    print("BALANCED")
else:
    print("UNBALANCED")