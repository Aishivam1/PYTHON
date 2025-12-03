heights = []
n = int(input("Enter number of persons: "))
for i in range(n):
    h = float(input(f"Enter height of person {i+1} (in cm): "))
    heights.append(h)

avg_height = sum(heights) / len(heights)
print(f"Average Height: {avg_height:.2f} cm")
