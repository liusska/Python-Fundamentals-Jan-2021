employee1_capacity = int(input())
employee2_capacity = int(input())
employee3_capacity = int(input())
clients_count = int(input())
hours = 0

total_employee_capacity = employee1_capacity + employee2_capacity + employee3_capacity

while clients_count > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1
    clients_count -= total_employee_capacity


print(f"Time needed: {hours}h.")