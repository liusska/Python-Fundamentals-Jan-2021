file_path = input().split("\\")

tokens = file_path[-1].split(".")
file_name = tokens[0]
extension = tokens[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")