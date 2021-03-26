code_message = input().split(" ")
final_message = ""

for message in code_message:
    number = ""
    char_list = []
    word = ""
    for ch in message:
        if ch.isdigit():
            number += ch
        else:
            char_list.append(ch)
    word += chr(int(number))
    a = char_list[0]
    char_list[0] = char_list[-1]
    char_list[-1] = a
    for char in char_list:
        word += char
    final_message += word
    final_message += " "

print(final_message)