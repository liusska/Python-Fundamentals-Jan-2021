import re
names = input()
pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

filtered_names = re.findall(pattern, names)

print(" ".join(filtered_names))