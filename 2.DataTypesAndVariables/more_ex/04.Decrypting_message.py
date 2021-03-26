key = int(input())
n = int(input())
message = ""

for i in range(n):
    ch = ord(input())
    current_ch = key + int(ch)
    message += chr(current_ch)

print(message)