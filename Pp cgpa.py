# COS202 Personal Pocket CGPA Calculator

print("=" * 45)
print("     PERSONAL POCKET CGPA CALCULATOR")
print("=" * 45)

num_courses = int(input("Enter number of courses: "))

total_grade_points = 0
total_units = 0

for i in range(1, num_courses + 1):
    print(f"\nCourse {i}")

    unit = int(input("Course Unit: "))
    score = float(input("Course Score: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    print("Grade:", grade)

    total_grade_points += point * unit
    total_units += unit

cgpa = total_grade_points / total_units

print("\n" + "=" * 45)
print("Total Units:", total_units)
print("Total Grade Points:", total_grade_points)
print("CGPA =", round(cgpa, 2))
print("=" * 45)
