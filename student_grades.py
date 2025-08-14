# Student Grades Management

# Initial dictionary
student_grades = {
    "John": "A",
    "Alice": "B",
    "Mike": "C"
}

while True:
    print("\n1. Add New Student")
    print("2. Update Student Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        student_grades[name] = grade
        print(f"{name} added successfully!")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"{name}'s grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\n--- Student Grades ---")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
