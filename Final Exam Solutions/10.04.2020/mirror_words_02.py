import re

pattern = r"(@|#)(?P<word>[A-za-z]{3,})\1{2}(?P<mirror>[A-za-z]{3,})\1"
data = input()

matchs = re.findall(pattern, data)

results = []
for match in matchs:
    if match[1] == (match[2])[::-1]:
        results.append(f"{match[1]} <=> {match[2]}")
if matchs:
    print(f"{len(matchs)} word pairs found!")
else:
    print("No word pairs found!")
if results:
    print("The mirror words are:")
    print(', '.join(results))

else:
    print("No mirror words!")

