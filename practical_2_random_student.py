import random

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
roll_numbers = list(range(1, 6))

selected_name = random.choice(names)
selected_roll = random.choice(roll_numbers)

print("\n--- Random Student Selection ---")
print(f"Selected Student: {selected_name}")
print(f"Roll Number: {selected_roll}")

while True:
    again = input("\nSelect another student? (yes/no): ")
    if again.lower() == "yes":
        selected_name = random.choice(names)
        selected_roll = random.choice(roll_numbers)
        print(f"Selected Student: {selected_name}")
        print(f"Roll Number: {selected_roll}")
    else:
        print("Thank you!")
        break
