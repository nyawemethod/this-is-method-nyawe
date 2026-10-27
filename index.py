student_data = [
    {"name": "Lemmy", "grade": 85.0},
    {"name": "Selge", "grade": 42.0},
    {"name": "Kevine", "grade": 38.0},
    {"name": "Mwiza", "grade": 92.0},
    {"name": "Clemance", "grade": 45.0},
    {"name": "Emmely", "grade": 78.0},
    {"name": "Threse", "grade": 31.0},
    {"name": "Fred", "grade": 88.0},
    {"name": "Henriette", "grade": 49.0},
    {"name": "method", "grade": 99.0},
]

total_students = 0
passed_students = 0
failed_students = 0
excellent_students = 0
total_score = 0.0

highest_grade = -1.0
highest_student = ""
lowest_grade = 101.0
lowest_student = ""

passed_list = []
failed_list = []
excellent_list = []

index = 0
while index < len(student_data):
    current_student = student_data[index]
    name = current_student["name"]
    grade = current_student["grade"]
    
    total_students += 1
    total_score += grade
    
    if grade > highest_grade:
        highest_grade = grade
        highest_student = name
        
    if grade < lowest_grade:
        lowest_grade = grade
        lowest_student = name
        
    if grade >= 90:
        excellent_students += 1
        excellent_list.append(f"{name} ({grade}%)")
        print(f"Processing database record: {name} -> EXCELLENT! Scored over 90% ({grade}%)")
    elif grade >= 50:
        passed_students += 1
        passed_list.append(f"{name} ({grade}%)")
        print(f"Processing database record: {name} -> Passing marks achieved ({grade}%)")
    else:
        failed_students += 1
        failed_list.append(f"{name} ({grade}%)")
        print(f"Processing database record: {name} -> Below passing threshold ({grade}%)")
        
    index += 1

print("\n" + "=" * 45)
print("             COMPLETE GRADBOOK REPORT        ")
print("=" * 45)
print(f"Total Evaluated Class Records : {total_students}")
print(f"Total Excellent (Over 90%)    : {excellent_students}")
print(f"Total Standard Pass (50%-89%) : {passed_students}")
print(f"Total Academic Deficiencies   : {failed_students}")

if total_students > 0:
    combined_pass = passed_students + excellent_students
    pass_percentage = (combined_pass / total_students) * 100
    class_average = total_score / total_students
    print(f"Class Success Percentage      : {pass_percentage:.2f}%")
    print(f"Class Mathematical Mean Score : {class_average:.2f}%")
    print("-" * 45)
    print(f"Highest Performing Student    : {highest_student} [{highest_grade}%]")
    print(f"Lowest Performing Student     : {lowest_student} [{lowest_grade}%]")
    print("-" * 45)
    print("Roster of Excellent Students (Over 90%):")
    if excellent_list:
        for student in excellent_list:
            print(f"  ★ {student}")
    else:
        print("  None")
    print("\nRoster of Passing Students (50% - 89%):")
    if passed_list:
        for student in passed_list:
            print(f"  • {student}")
    else:
        print("  None")
    print("\nRoster of Failing Students:")
    if failed_list:
        for student in failed_list:
            print(f"  • {student}")
    else:
        print("  None")
else:
    print("Database Empty: No metrics recorded during execution loop.")
print("=" * 45)
