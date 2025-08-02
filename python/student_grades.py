students = {}

while True:
    choice = input("\n1.Add  2.Update  3.Print  4.Exit: ")

    if choice == "1":
        name = input("Name: ")
        grade = input("Grade: ")
        students[name] = grade
        print("Student added.")

    elif choice == "2":
        name = input("Name to update: ")
        if name in students:
            students[name] = input("New Grade: ")
            print("Grade updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        for n, g in students.items():
            print(f"{n}: {g}")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
