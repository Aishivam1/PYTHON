name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = []
for i in range(3):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 3

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Marksheet ---")
print(f"Name: {name}\nRoll No: {roll}")
print("Marks:", marks)
print(f"Total: {total}\nPercentage: {percentage:.2f}%\nGrade: {grade}")
