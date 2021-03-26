word = input()
indices = []
count = 0

for ch in word:
    if ch.isupper():
        indices.append(count)
    count += 1

print(indices)
