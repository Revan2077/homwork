# Get the number
number = int(input("Enter your number: "))

# Print multiplication table
print(f"Multiplication table for {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")