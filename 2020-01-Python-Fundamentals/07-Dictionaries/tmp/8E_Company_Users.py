companies = {}

while True:
    command = input()
    if command == "End":
        break
    company, employee_id = command.split(" -> ")
    if company not in companies:
        companies[company] = [employee_id]
    else:
        if employee_id not in companies[company]:
            companies[company] += [employee_id]

for company, employees in sorted(companies.items()):
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")