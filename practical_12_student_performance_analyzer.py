students = {}

while True:
    print("\n=== Student Performance Analyzer ===")
    print("1. Add student")
    print("2. View students")
    print("3. Calculate grade")
    print("4. Delete student")
    print("5. Exit")
    
    choice = input("\nEnter choice (1/2/3/4/5): ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks = []
        for i in range(3):
            m = int(input(f"Enter marks of subject {i+1}: "))
            marks.append(m)
        average = sum(marks) / len(marks)
        students[name] = {"marks": marks, "average": average}
        print("✓ Student added!")
        
    elif choice == "2":
        if students:
            print("\n--- All Students ---")
            for name, data in students.items():
                print(f"{name}: Average = {data['average']:.2f}")
        else:
            print("No students!")
            
    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            avg = students[name]['average']
            if avg >= 75:
                grade = "A"
            elif avg >= 60:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "Fail"
            print(f"\n{name} - Average: {avg:.2f}, Grade: {grade}")
        else:
            print("Student not found!")
            
    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("✓ Student deleted!")
        else:
            print("Student not found!")
            
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
