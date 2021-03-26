companies_id = {}

while True:
    command = input()
    if command == "End":
        break
    company, employee_id = command.split(" -> ")
    if company not in companies_id:
        companies_id[company] = []
    if employee_id not in companies_id[company]:
        companies_id[company].append(employee_id)

sorted_companies = dict(sorted(companies_id.items(), key=lambda x: x[0]))

for key, value in sorted_companies.items():
    print(f"{key}")
    for val in value:
        print(f"-- {val}")