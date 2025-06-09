student_marks = { "alice": 85, "Bob": 78, "Charlie": 92,}

student_name = input("Enter the student's name: ")


if student_name in student_marks:
    print(student_name,"'s marks:", student_marks[student_name])
else:
    print("student not found")

