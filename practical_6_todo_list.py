todo_list = []

while True:
    print("\n=== Todo List ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("\nEnter choice (1/2/3/4): ")
    
    if choice == "1":
        task = input("Enter new task: ")
        todo_list.append(task)
        print("✓ Task added!")
        
    elif choice == "2":
        if todo_list:
            print("\nYour tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet!")
            
    elif choice == "3":
        if todo_list:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(todo_list):
                del todo_list[task_num - 1]
                print("✓ Task deleted!")
            else:
                print("Invalid number!")
        else:
            print("No tasks to delete!")
            
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
