# Get weight and height
weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

# BMI
bmi = weight / (height ** 2)

# Print
print(f"Your BMI is: {bmi:.2f}")
