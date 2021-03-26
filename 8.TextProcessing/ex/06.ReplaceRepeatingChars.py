text = input()

filtered_text = text[0]

for ch in text:
    if ch != filtered_text[-1]:
        filtered_text += ch

print(filtered_text)