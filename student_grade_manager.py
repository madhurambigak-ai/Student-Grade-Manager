
# Student Grade Manager
# Python Assignment

students = []


# Step 1: Calculate student grade
def get_grade(mark):

    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"


# Step 2: Add a new student
def add_student():

    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    while True:

        mark_input = input("Enter student mark (0-100): ").strip()

        try:
            mark = int(mark_input)

            if mark < 0 or mark > 100:
                print("Invalid mark! Please enter a value between 0 and 100.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    grade = get_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print(f"\nStudent '{name}' added successfully!")
    print(f"Grade: {grade}")


# Step 3: Display student results
def show_results():

    print("\n========== STUDENT RESULTS ==========")

    if not students:
        print("No student records found. Please add students first.")
        return

    # Display table headings
    print("-" * 40)
    print(f"{'Name':<20} {'Mark':<8} {'Grade':<8}")
    print("-" * 40)

    # Display student details
    for student in students:

        print(
            f"{student['name']:<20} "
            f"{student['mark']:<8} "
            f"{student['grade']:<8}"
        )

    print("-" * 40)

    # Calculate class statistics
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"\nClass Average : {average:.1f}")
    print(f"Highest Mark  : {highest}")
    print(f"Lowest Mark   : {lowest}")

    print("=" * 40)


# Step 4: Main menu
def main():

    print("\nWelcome to Student Grade Manager!")

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")
        print("===============================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            show_results()

        elif choice == "3":

            print("\nThank you for using Student Grade Manager!")
            print("Goodbye!")
            break

        else:

            print("Invalid choice! Please select 1, 2, or 3.")


# Step 5: Run the program safely
if __name__ == "__main__":

    try:
        main()

    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram stopped safely. Goodbye!")
