"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

print("*" * 40)
print("\t   Currency Converter")
print("*" * 40)

convert = input("What currency do you want to change to? (type 1: USD to THB, type 2: THB to USD): ")

if convert == '1' :
    usd = float(input("Enter US Dollars(USD): "))
    thb = usd * 35.5
    print(f"Thai Bant(THB): {thb:.2f}")
elif convert == '2' :
    thb  = float(input("Enter Thai Baht(THB): "))
    usd = thb / 35.5
    print(f"US Dollar(USD): {usd:.2f}")
else :
    print("Invalid")