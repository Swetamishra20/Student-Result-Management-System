student = {}

def calculator_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"


while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Check Result")
    print("5. Class Topper")
    print("6. Exit")

    choice = input("Enter your choice:")


    if choice == "1":
        roll = input("Enter your choice:")

        if roll in student:
            print("Roll number already exists!")
            continue

        name = input("Entetr student name:")

        marks = []
        for i in range(1, 6):
            mark = int(input(f"Enter Subject {i} Marks:"))
            if mark < 0 or mark >100:
                print("Invalid marks! Enter 0-100.")
                break
            marks.append(mark)
        else:
            total  = sum(marks)
            percentage = total / 5
            grade = calculator_grade(percentage)

            student[roll] = {
                "name": name,
                "marks": marks,
                "total": total,
                "percentage": percentage,
                "grade": grade
            }

            print("Student added successfully!")

    elif choice == "2":
            if not student: 
                print("No student found!")
            else:
                for roll, data in student.items():
                    print(roll,data["name"],
                          data["percentage"],"%")

    elif choice == "3":
         roll = input("Enter Roll Number: ")


         if roll in student:
             print("Student:", student[roll]["name"])
             print("Marks:" , student[roll]["marks"])
         else:
             print("student not found!")


    elif choice == "4":
        roll = input("Enter Roll Number:")

        if roll in student:
            data = student[roll]
            print("Name:", data["name"])
            print("Total:", data["total"])
            print("percentage:", data["percentage"], "%")
            print("Grade:", data["grade"])
        else:
            print("Student not found!")

                    
    elif choice == "5":
        if student:
            topper = max(
                student,
                key=lambda r:
                student[r]["percentage"]
            )
            print("Class Topper:", student[topper]["name"])
            print("percentage:",
                  student[topper]["percentage"], "%")
                  

        else:
            print("No student records!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

        