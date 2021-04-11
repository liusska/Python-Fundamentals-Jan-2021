import re


pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
n = int(input())
for _ in range(n):
    data = input()
    match = re.findall(pattern, data)
    if match:
        digit = ""
        for ch in str(match):
            if ch.isdigit():
                digit += ch
        if digit == "":
            print("Product group: 00")
        else:
            print(f"Product group: {digit}")
    else:
        print("Invalid barcode")
