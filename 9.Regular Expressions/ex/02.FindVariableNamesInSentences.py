import re

data = input()
pattern = r"\b_[A-Za-z0-9]+\b"

valid_data = re.finditer(pattern, data)
valid_data_collection = []
for value in valid_data:
    v = value.group(0)
    valid_data_collection.append(v[1:])

print(",".join(valid_data_collection))