expenses = []

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total spent")
    print("4. Delete expense")
    print("5. Exit")
    
    choice = input("\nEnter choice (1/2/3/4/5): ")
    
    if choice == "1":
        category = input("Enter category (e.g., Food, Transport): ")
        amount = float(input("Enter amount: "))
        expenses.append({"category": category, "amount": amount})
        print("✓ Expense added!")
        
    elif choice == "2":
        if expenses:
            print("\n--- Your Expenses ---")
            for i, exp in enumerate(expenses, 1):
                print(f"{i}. {exp['category']}: ${exp['amount']}")
        else:
            print("No expenses yet!")
            
    elif choice == "3":
        if expenses:
            total = sum(exp['amount'] for exp in expenses)
            print(f"\nTotal Spent: ${total:.2f}")
        else:
            print("No expenses!")
            
    elif choice == "4":
        if expenses:
            for i, exp in enumerate(expenses, 1):
                print(f"{i}. {exp['category']}: ${exp['amount']}")
            exp_num = int(input("Enter expense number to delete: "))
            if 1 <= exp_num <= len(expenses):
                del expenses[exp_num - 1]
                print("✓ Expense deleted!")
            else:
                print("Invalid number!")
        else:
            print("No expenses to delete!")
            
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
