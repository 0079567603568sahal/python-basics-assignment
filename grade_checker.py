# Grade Checker Program

# Taking input from the user
score = int(input("Enter the score: "))

# Using if-else statements to determine grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Printing the result
print(f"Grade: {grade}")
