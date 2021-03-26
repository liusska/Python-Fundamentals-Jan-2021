courses = {}

while True:
    command = input()
    if command == "end":
        break
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    for v in sorted(value):
        print(f"-- {v}")