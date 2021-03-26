students_grade = {}
n = int(input())
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students_grade:
        students_grade[name] = []
    students_grade[name].append(grade)


sorted_students = dict(sorted(students_grade.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True))

for key, value in sorted_students.items():
    average_score = sum(value) / len(value)
    if average_score >= 4.50:
        print(f"{key} -> {average_score:.2f}")