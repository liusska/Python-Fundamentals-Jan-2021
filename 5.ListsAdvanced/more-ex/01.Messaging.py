numbers = input().split(" ")
text = input()
text_as_list = [ch for ch in text]
word = ""
for num in numbers:
    result = 0
    for n in num:
        result += int(n)

    if result < len(text_as_list):
        word += text_as_list[result]
        text_as_list.remove(text_as_list[result])
    else:
        current_index = len(text_as_list) // result
        word += text_as_list[current_index + 1]
        text_as_list.remove(text_as_list[current_index])

print(word)

