# COS202 Mathematical Calculator

def calculator():
    print("=" * 40)
    print("      MATHEMATICAL CALCULATOR")
    print("=" * 40)

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Modulus (%)")
        print("7. Clear")
        print("8. OFF")

        choice = input("Enter your choice (1-8): ")

        if choice == "8":
            print("Calculator OFF. Goodbye!")
            break

        elif choice == "7":
            print("\n" * 50)
            continue

        elif choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print("Answer =", num1 + num2)

                elif choice == "2":
                    print("Answer =", num1 - num2)

                elif choice == "3":
                    print("Answer =", num1 * num2)

                elif choice == "4":
                    if num2 == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        print("Answer =", num1 / num2)

                elif choice == "5":
                    print("Answer =", num1 ** num2)

                elif choice == "6":
                    print("Answer =", num1 % num2)

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice!")

calculator()
