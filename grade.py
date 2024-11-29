def grade_manager():
    grades = {}

    def calculate_letter_grade(average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def calculate_gpa(average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    while True:
        print("\nStudent Grades Manager")
        print("1. Add or update a grade")
        print("2. View all grades")
        print("3. Calculate average grade")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '4':
            print("Exiting the grade manager. Goodbye!")
            break

        if choice == '1':
            subject = input("Enter the subject or assignment name: ")
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    print(f"Grade for {subject} has been recorded.")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")

        elif choice == '2':
            if not grades:
                print("No grades recorded yet.")
            else:
                print("\nGrades:")
                for subject, grade in grades.items():
                    print(f"{subject}: {grade}")

        elif choice == '3':
            if not grades:
                print("No grades to calculate an average.")
            else:
                total = sum(grades.values())
                count = len(grades)
                average = total / count
                letter_grade = calculate_letter_grade(average)
                gpa = calculate_gpa(average)

                print(f"\nAverage Grade: {average:.2f}")
                print(f"Letter Grade: {letter_grade}")
                print(f"GPA: {gpa:.2f}")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    grade_manager()