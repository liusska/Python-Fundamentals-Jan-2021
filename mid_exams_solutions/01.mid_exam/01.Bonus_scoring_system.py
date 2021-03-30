from math import ceil

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_student_bonus = 0
max_attendances_bonus = 0

for i in range(students_count):
    current_attendances = int(input())
    current_students_bonus = current_attendances / lectures_count * (5 + additional_bonus)
    if current_students_bonus > max_student_bonus:
        max_student_bonus = current_students_bonus
        max_attendances_bonus = current_attendances

print(f"Max Bonus: {ceil(max_student_bonus)}.")
print(f"The student has attended {max_attendances_bonus} lectures.")

