scores = {}
users = {}


def add_score(language, points, dict):
    if language not in dict:
        dict[language] = []
    dict[language].append(points)
    return dict


def add_user(user, points, dict):
    if user not in dict:
        dict[user] = 0
    if points > dict[user]:
        dict[user] = points
    return dict


while True:
    command = input()
    if command == "exam finished":
        break
    tokens = command.split("-")
    name = tokens[0]
    if len(tokens) == 3:
        lang = tokens[1]
        score = int(tokens[2])
        users = add_user(name, score, users)
        scores = add_score(lang, score, scores)
    else:
        if name in users:
            users.pop(name)

print("Results:")
sorted_users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
for key, value in sorted_users.items():
    print(f"{key} | {value}")
print("Submissions:")
sorted_scores = dict(sorted(scores.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in sorted_scores.items():
    print(f"{key} - {len(value)}")