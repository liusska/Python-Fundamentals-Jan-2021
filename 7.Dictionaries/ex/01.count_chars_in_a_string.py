word = input()

chars = {}

for ch in word:
    if not ch == " ":
        if ch not in chars:
            chars[ch] = 0
        chars[ch] += 1

for key, val in chars.items():
    print(f"{key} -> {val}")