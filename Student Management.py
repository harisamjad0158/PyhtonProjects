class Student:
    def __init__(self, roll_number, name, age, grade):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def remove_student_by_roll_number(self, roll_number):
        student = self.find_student_by_roll_number(roll_number)
        if student:
            self.students.remove(student)
            print(f"Student with roll number {roll_number} removed.")
        else:
            print(f"Student with roll number {roll_number} not found.")

    def display_all_students(self):
        print("All Students:")
        for student in self.students:
            print(f"Roll Number: {student.roll_number}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")


def main():
    student_management = StudentManagementSystem()

    while True:
        print("\n1. Add Student")
        print("2. Find Student by Roll Number")
        print("3. Remove Student by Roll Number")
        print("4. Display All Students")
        print("5. Exit")

        choice = int(input("Enter your choice (1/2/3/4/5): "))

        if choice == 1:
            roll_number = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")

            student = Student(roll_number, name, age, grade)
            student_management.add_student(student)
            print("Student added successfully.")

        elif choice == 2:
            roll_number = int(input("Enter Roll Number to find: "))
            student = student_management.find_student_by_roll_number(roll_number)
            if student:
                print(f"Student found - Roll Number: {student.roll_number}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
            else:
                print("Student not found.")

        elif choice == 3:
            roll_number = int(input("Enter Roll Number to remove: "))
            student_management.remove_student_by_roll_number(roll_number)

        elif choice == 4:
            student_management.display_all_students()

        elif choice == 5:
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

