start_char = input()
end_char = input()


def solve(start, end):
    a = ord(start)
    b = ord(end)
    string = ""
    for i in range(a + 1, b):
        string += chr(i)
        string += " "
    return string


print(solve(start_char, end_char))