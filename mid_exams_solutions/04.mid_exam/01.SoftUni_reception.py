employee1 = int(input())
employee2 = int(input())
employee3 = int(input())

students = int(input())
hours = 0

total_employee_per_hours = employee1 + employee2 + employee3
while students > 0:
    students -= total_employee_per_hours
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")