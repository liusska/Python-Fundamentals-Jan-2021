line = input().split(", ")


def is_palindrome(number):
    reversed_number = number[::-1]
    if number == reversed_number:
        print("True")
    else:
        print("False")


for i in range(0, len(line)):
    is_palindrome(line[i])