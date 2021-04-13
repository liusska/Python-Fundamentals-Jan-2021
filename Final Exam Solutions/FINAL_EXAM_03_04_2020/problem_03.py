def message(sender_name, receiver_name):
    sender = [s for s in users if s.name == sender_name][0]
    receiver = [r for r in users if r.name == receiver_name][0]
    if sender and receiver:
        sender.sent += 1
        check_capacity(sender.name)
        receiver.received += 1
        check_capacity(receiver.name)


def check_capacity(user_check):
    user_to_check = [u for u in users if u.name == user_check][0]
    if user_to_check.total() >= capacity:
        print(f"{user_check} reached the capacity!")
        users.remove(user_to_check)


def add_user(name_u, sent_u, received_u):
    user_to_add = [u for u in users if u.name == name_u]
    if not user_to_add:
        user_to_add = User(name_u, sent_u, received_u)
        users.append(user_to_add)


class User:
    def __init__(self, name, sent, received):
        self.name = name
        self.sent = sent
        self.received = received

    def total(self):
        return self.sent + self.received

    def __repr__(self):
        return f"{self.name} - {self.total()}"


users = []
capacity = int(input())


while True:
    command = input()
    if command == "Statistics":
        break
    tokens = command.split("=")

    if tokens[0] == "Add":
        current_name = tokens[1]
        current_sent = int(tokens[2])
        current_receive = int(tokens[3])
        add_user(current_name, current_sent, current_receive)
    elif tokens[0] == "Message":
        current_sender = tokens[1]
        current_receiver = tokens[2]
        message(current_sender, current_receiver)
    elif tokens[0] == "Empty":
        if tokens[1] == "All":
            users = []
        else:
            user_to_del = [u for u in users if u.name == tokens[1]]
            if user_to_del:
                users.remove(user_to_del[0])

if len(users) > 0:
    print(f"Users count: {len(users)}")
    sorted_user = sorted(users, key=lambda u: (-u.received, u.name))
    for user in sorted_user:
        print(user)
