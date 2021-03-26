text = input()
alpha = ""
digits = ""
others = ""

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        alpha += char
    else:
        others += char
print(digits)
print(alpha)
print(others)

