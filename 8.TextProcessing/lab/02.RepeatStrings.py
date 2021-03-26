text = input().split(" ")
concat_word = ""
for word in text:
    concat_word += word * len(word)

print(concat_word)