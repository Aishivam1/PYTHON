contacts = {}

while True:
    print("\n=== Contact Book ===")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("\nEnter choice (1/2/3/4/5): ")
    
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("✓ Contact added!")
        
    elif choice == "2":
        if contacts:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts!")
            
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found!")
            
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("✓ Contact deleted!")
        else:
            print("Contact not found!")
            
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
