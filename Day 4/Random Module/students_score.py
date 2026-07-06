print("Welcome to school of physical science")
total_students = int(input("How many students are offering this course? "))
passed = 0
failed = 0
highest_score = 0
lowest_score = 100
total_score = 0

for student in range(total_students):

    while True:
        students_score = int(input(f"Enter scores for student {student + 1}: "))

        if 0 <= students_score <= 100:
            break
        else:
            print("Invalid score")

    if students_score >= 70:
        print("Your score is: A ")
    elif students_score >= 60:
        print("Your score is: B ")
    elif students_score >= 50:
        print("Your score is: C ")
    elif students_score >= 45:
        print("Your score is: D ")
    else:
        print("Your score is: F ")

    if students_score >= 50:
        passed += 1
    else:
        failed += 1

    total_score += students_score

    if students_score > highest_score:
        highest_score = students_score

    if students_score < lowest_score:
        lowest_score = students_score

average_score = total_score / total_students

print(f"""
Total students: {total_students}
Passed: {passed}
Failed: {failed}
Highest score: {highest_score}
Lowest score: {lowest_score}
Average score: {average_score}
""")

