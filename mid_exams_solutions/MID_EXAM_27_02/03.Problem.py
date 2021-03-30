message = []

while True:
    command = input()
    if command == "end":
        break
    tokens = command.split()
    if tokens[0] == "Chat":
        message.append(tokens[1])
    elif tokens[0] == "Delete":
        if tokens[1] in message:
            message.remove(tokens[1])
    elif tokens[0] == "Edit":
        for i in range(len(message)):
            if message[i] == tokens[1]:
                message[i] = tokens[2]
    elif tokens[0] == "Pin":
        if tokens[1] in message:
            message.remove(tokens[1])
            message.append(tokens[1])
    elif tokens[0] == "Spam":
        for word in tokens[1:]:
            message.append(word)

print('\n'.join(message))