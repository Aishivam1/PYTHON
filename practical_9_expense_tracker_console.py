"""
Practical 9: Expense Tracker (Console)
A simple program to track and manage expenses
"""


def expense_tracker():
    print("\n=== EXPENSE TRACKER ===\n")
    
    expenses = []
    
    while True:
        print("What do you want to do?")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Delete expense")
        print("5. Exit")
        print()
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            # Add expense
            try:
                category = input("Enter category (Food/Transport/Shopping/etc): ")
                amount = float(input("Enter amount (₹): "))
                description = input("Enter description (optional): ")
                
                if category and amount > 0:
                    expenses.append({
                        'category': category,
                        'amount': amount,
                        'description': description if description else 'N/A'
                    })
                    print(f"✓ Added ₹{amount} expense!\n")
                else:
                    print("Please enter valid category and amount!\n")
            except:
                print("Invalid input!\n")
        
        elif choice == '2':
            # View all expenses
            if expenses:
                print("\n" + "=" * 60)
                print("ALL EXPENSES:")
                print("=" * 60)
                print(f"{'#':<3} {'Category':<15} {'Amount':<12} {'Description':<25}")
                print("-" * 60)
                
                total = 0
                for i, exp in enumerate(expenses, 1):
                    print(f"{i:<3} {exp['category']:<15} ₹{exp['amount']:<11.2f} {exp['description']:<25}")
                    total += exp['amount']
                
                print("-" * 60)
                print(f"TOTAL: ₹{total:.2f}")
                print("=" * 60 + "\n")
            else:
                print("\nNo expenses yet!\n")
        
        elif choice == '3':
            # Summary by category
            if expenses:
                print("\n" + "=" * 50)
                print("EXPENSE SUMMARY BY CATEGORY:")
                print("=" * 50)
                
                categories = {}
                for exp in expenses:
                    cat = exp['category']
                    categories[cat] = categories.get(cat, 0) + exp['amount']
                
                total_all = sum(categories.values())
                
                for category in sorted(categories.keys()):
                    amount = categories[category]
                    percentage = (amount / total_all) * 100
                    print(f"{category:<20} ₹{amount:<12.2f} ({percentage:5.1f}%)")
                
                print("-" * 50)
                print(f"{'TOTAL':<20} ₹{total_all:.2f}")
                print("=" * 50 + "\n")
            else:
                print("\nNo expenses yet!\n")
        
        elif choice == '4':
            # Delete expense
            if expenses:
                print("\nYour expenses:")
                for i, exp in enumerate(expenses, 1):
                    print(f"{i}. ₹{exp['amount']} - {exp['category']}")
                
                try:
                    exp_num = int(input("\nEnter number to delete: "))
                    if 1 <= exp_num <= len(expenses):
                        removed = expenses.pop(exp_num - 1)
                        print(f"✓ Deleted: ₹{removed['amount']} - {removed['category']}\n")
                    else:
                        print("Invalid number!\n")
                except:
                    print("Please enter a valid number!\n")
            else:
                print("\nNo expenses to delete!\n")
        
        elif choice == '5':
            print("\nThank you!\n")
            break
        
        else:
            print("\nInvalid choice! Please try again.\n")


# Run the program
if __name__ == "__main__":
    expense_tracker()
