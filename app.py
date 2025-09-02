num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("\nEnter your operation(+,-,*,/): ")

if operation == "+" :
      result = num1 + num2
      print(f"{num1}+{num2} = {result}")
elif operation == "-" :
      result = num1 - num2
      print(f"{num1} - {num2} = {result}")
elif operation == "*" :
      result = num1 * num2
      print(f"{num1} * {num2} = {result}")
elif operation == "/" :
      result = num1 / num2
      print(f"{num1} / {num2} = {result}")
else:
    print("you have enter wrong operation")