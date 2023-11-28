# Student Database
students = {}

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    students[name] = {'Age': age, 'Grade': grade}
    print(f"Student {name} added successfully!")

# Function to view details of a specific student
def view_student():
    name = input("Enter student name to view details: ")
    if name in students:
        print(f"\nDetails of {name}:")
        print(f"Age: {students[name]['Age']}")
        print(f"Grade: {students[name]['Grade']}")
    else:
        print(f"Student {name} not found in the database.")

# Function to list all students
def list_all_students():
    print("\nList of all students:")
    if not students:
        print("No students in the database.")
    else:
        for name, details in students.items():
            print(f"{name}: Age - {details['Age']}, Grade - {details['Grade']}")


def update_student():
    name = input("Enter student name to update information: ")
    if name in students:
        print(f"Current details of {name}:")
        print(f"Age: {students[name]['Age']}")
        print(f"Grade: {students[name]['Grade']}")
        
        new_age = int(input("Enter new age (press Enter to keep the current age): ") )
        new_grade = input("Enter new grade (press Enter to keep the current grade): ") 

        students[name]['Age'] = new_age
        students[name]['Grade'] = new_grade

        print(f"Information for {name} updated successfully!")
    else:
        print(f"Student {name} not found in the database.")

# Function to delete a student
def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully!")
    else:
        print(f"Student {name} not found in the database.")

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_all_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
