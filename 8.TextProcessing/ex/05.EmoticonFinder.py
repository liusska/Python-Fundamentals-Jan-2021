text = input()

for i in range(0, len(text)):
    if text[i] == ":":
        emoticon = text[i]
        emoticon += text[i + 1]
        i += 1
        print(emoticon)

