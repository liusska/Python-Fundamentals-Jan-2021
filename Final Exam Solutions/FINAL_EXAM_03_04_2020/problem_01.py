def make(data, type_case):
    if type_case == "Lower":
        data = data.lower()
    elif type_case == "Upper":
        data = data.upper()
    print(data)
    return data


def get_domain(count):
    domain = email[-count:]
    print(domain)


def get_username():
    if "@" in email:
        idx = email.index("@")
        result = email[:idx]
        print(result)
    else:
        print(f"The email {email} doesn't contain the @ symbol.")


def replace_char(data, char):
    data = data.replace(char, "-")
    print(data)
    return data


def encrypt():
    for ch in email:
        print(ord(ch), end=" ")


email = input()
while True:
    command = input()
    if command == "Complete":
        break

    tokens = command.split()
    if tokens[0] == "Make":
        email = make(email, tokens[1])
    elif tokens[0] == "GetDomain":
        get_domain(int(tokens[1]))
    elif tokens[0] == "GetUsername":
        get_username()
    elif tokens[0] == "Replace":
        email = replace_char(email, tokens[1])
    elif tokens[0] == "Encrypt":
        encrypt()
