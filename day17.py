def new_student():
    try:
        name = input("Enter Student name: ")
        grade1 = int(input("Enter math grade: "))
        grade2 = int(input("Enter science grade: "))
        grade3 = int(input("Enter English grade: "))
        with open("day17.py" , "a" , encoding = "utf-8") as f:
            f.write(f"{name},{grade1},{grade2},{grade3}\n")  # Formatted string
        print(f"{name}, {grade1}, {grade2}, {grade3}")
    except ValueError:
        print("Invalid data type. Please enter integers for grades.")
def view_students():
    with open("day17.py" ,"r" , encoding = "utf-8") as f:
        for line in f:
            print(line)

def student_average():
    name = input("Enter student name to calculate average: ")
    try:
        with open("day17.py", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(',')
                if data[0] == name:
                    grades = list(map(int, data[1:]))
                    average = sum(grades) / len(grades)
                    print(f"{name}'s average: {average:.2f}")
                    return
            print(f"Student '{name}' not found.")
    except FileNotFoundError:
        print("No students data found.")
def main():
    print("---Welcome to your Notebook!")
    while True:
        print("\n1.Add new student")
        print("2.View all student")
        print("3.Student Average")
        print("4.Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            new_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_average()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invaid choice")

if __name__ == "__main__":
    main()
carl,21,21,21
