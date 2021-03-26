password = input()


def validate(input_pass):
    is_valid = True
    if not (6 <= len(input_pass) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    count = 0
    for ch in input_pass:
        if ch.isdigit():
            count += 1
    if count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    for ch in input_pass:
        if not (48 <= ord(ch) <= 57 or 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122):
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    if is_valid:
        print("Password is valid")


validate(password)