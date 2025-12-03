print("\n=== Simple Calculator ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("\nEnter your choice (1/2/3/4): ")

if choice == "1":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == "2":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif choice == "3":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Cannot divide by zero!")
else:
    print("\nInvalid choice!")
