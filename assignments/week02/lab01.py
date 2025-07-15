"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

print("*" * 40)
print("\t     BMI Calculator")
print("*" * 40)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight / height ** 2
print(f"Your BMI is {BMI}")

if BMI < 18.5 :
    print("Underweight")
elif 18.5 <= BMI <= 24.9 :
    print("Normal weight")
elif 25.0 <= BMI <= 29.9 :
    print("Overweight")
else :
    print("Obese")
