students = {}

while True:
    print("\n--- STUDENT RESULT SYSTEM ---")
    print("1. Add Student Result")
    print("2. Display All Results")
    print("3. Search Result by Roll No")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # ADD
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        m1 = int(input("Enter Math Marks: "))
        m2 = int(input("Enter Science Marks: "))
        m3 = int(input("Enter English Marks: "))
        m4 = int(input("Enter History Marks: "))
        m5 = int(input("Enter Geography Marks: "))

        students[roll] = {
            "name": name,
            "marks": [m1, m2, m3, m4, m5]
        }

        print("Student result added successfully!")

    # DISPLAY
    elif choice == "2":
        if not students:
            print("No records found!")
        else:
            for roll, data in students.items():
                print("\nRoll No:", roll)
                print("Name:", data["name"])
                print("Marks:", data["marks"])

    # SEARCH
    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        if roll in students:
            data = students[roll]
            print("\nRoll No:", roll)
            print("Name:", data["name"])
            print("Math:", data["marks"][0])
            print("Science:", data["marks"][1])
            print("English:", data["marks"][2])
            print("History:", data["marks"][3])
            print("Geography:", data["marks"][4])
        else:
            print("Student not found!")

    # EXIT
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
