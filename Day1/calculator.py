print("=== Simple Calculator")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter a choice (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting Calculator. Goodbye!")
        break
   
    num1 = float(input("Enter a First number: "))
    num2 = float(input("Enter a second number: "))

    if choice == "1":
        result = num1 + num2
        print(f"Result: {num1}+{num2}={result}")

    elif choice == "2":
        result = num1 - num2
        print(f"Result: {num1}-{num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif choice == "4":
        if num2 != 0:
            result = num1/num2
            print(f"Result: {num1} % {num2} = {result}")
        else:
            print("Divion by zero is not allowed!.")

    else:
        print("Invalid choice! Please select a valid option.")