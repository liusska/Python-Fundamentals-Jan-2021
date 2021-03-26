word = input()
lower_word = ""
count = 0

for w in word:
    lower_word += w.lower()
    if "sand" in lower_word or "water" in lower_word or "fish" in lower_word or "sun" in lower_word:
        count += 1
        lower_word = ""

print(count)