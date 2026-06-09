students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        students.append({"Name": name, "Roll": roll})
        print("Student added successfully!")

    elif choice == "2":
        for student in students:
            print(student)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
