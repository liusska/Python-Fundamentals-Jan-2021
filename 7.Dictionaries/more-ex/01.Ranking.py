contests = {}
student_contests = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contests[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    tokens = command.split("=>")
    contest = tokens[0]
    password = tokens[1]
    user = tokens[2]
    points = int(tokens[3])
    if contest in contests and contests[contest] == password:
        if user not in student_contests:
            student_contests[user] = {contest: int(points)}
        else:
            if contest in student_contests[user]:
                if student_contests[user][contest] < points:
                    student_contests[user][contest] = points
            else:
                student_contests[user][contest] = points

ordered_ratings = {n: v for n, v in (sorted(student_contests.items()))}
for key, value in ordered_ratings.items():
    v = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    ordered_ratings[key] = v

max_points = 0
best_candidate = ''

for key, value in ordered_ratings.items():
    current_points = 0
    for sk, sv in value.items():
        current_points += sv
    if current_points > max_points:
        max_points = current_points
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for key, value in ordered_ratings.items():
    print(key)
    for c, p in value.items():
        print(f"#  {c} -> {p}")