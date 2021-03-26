import re

numbers = input()
pattern = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"

filtered_numbers = re.finditer(pattern, numbers)

filtered_numbers = [n.group(0) for n in filtered_numbers]

print(", ".join(filtered_numbers))

