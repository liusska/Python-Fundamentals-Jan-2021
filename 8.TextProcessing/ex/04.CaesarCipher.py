text = input()

encrypted_message = ""

for ch in text:
    ch = int(ord(ch))
    encrypted_ch = ch + 3
    encrypted_message += chr(encrypted_ch)

print(encrypted_message)