print("---Your calculator is here---")
while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice = input("What would you like to do?(1-5) ")
    if choice == "1":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        def add(first_number,second_number):
            return first_number + second_number
        print(f"The sum is: {add(first_number,second_number)}")
    elif choice == "2":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        def subtract(first_number,second_number):
            return first_number - second_number
        print(f"The sub is: {subtract(first_number,second_number)}")
    elif choice == "3":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        def multiply(first_number ,second_number):
            return first_number * second_number
        print(f"Your answer is: {multiply(first_number,second_number)}")
    elif choice == "4":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        def division(first_number,second_number):
            return first_number / second_number
        print(f"Your answer is: {division(first_number,second_number)}")
    elif choice == "5":
        print("GoodBye!")
        break    
    else:
        print("Invalid input")