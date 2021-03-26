string = input()
num = int(input())


def repeat_string(char, repeat_num):
    new_str = ""
    for i in range(0, repeat_num):
        new_str += char
    return new_str


print(repeat_string(string, num))
