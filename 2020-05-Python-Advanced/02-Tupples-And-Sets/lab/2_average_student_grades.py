students_dict = {}
for _ in range(1, int(input()) + 1):
    student_info = input().split(' ')
    current_student = student_info[0]
    grade = f"{float(student_info[1]):.2f}"
    if current_student not in students_dict:
        students_dict[current_student] = []
    students_dict[current_student].append(f"{float(grade):.2f}")

for student, grade in students_dict.items():
    grade_clr = " ".join(grade)
    grade_float = list(map(float, grade))
    average = sum(grade_float) / len(grade_float)
    print(f"{student} -> {grade_clr} (avg: {average:.2f})")

# v1.0
# def average(foo_grade):
#     return sum(map(float, foo_grade)) / len(foo_grade)
#
#
# if __name__ == '__main__':
#     student_record = {}
#     for _ in range(int(input())):
#         inp = input().split()
#         student = inp[0]
#         grade = inp[1]
#
#         if student not in student_record:
#             student_record[student] = []
#         student_record[student] += [grade]
#
#     for student, grade in student_record.items():
#         name = student
#         grades = " ".join(grade)
#         avg = average(grade)
#         print(f"{name} -> {grades} (avg: {round(avg, 2):.2f})")
