import re

data = input()
pattern = r" ([a-zA-Z0-9]+[-\._]*[a-zA-Z0-9]+@[a-zA-Z]+-*[a-zA-Z]+(\.+[a-zA-Z]+-?[a-zA-Z]+)+)"

valid_data = [x[0] for x in re.finditer(pattern, data)]
print("\n".join(valid_data))