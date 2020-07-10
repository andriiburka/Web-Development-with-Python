import collections as c

students = c.defaultdict(list)
entries = int(input())

for i in range(entries):
    student = input()
    grade = float(input())
    students[student].append(grade)

students_temp = {}
for key, value in students.items():
    if sum(value) / len(value) >= 4.5:
        students_temp[key] = value

for i in sorted(students_temp, key=lambda x: sum(students_temp[x]) / len(students_temp[x]), reverse=True):
    print(f"{i} -> {sum(students_temp[i]) / len(students_temp[i]):.2f}")
