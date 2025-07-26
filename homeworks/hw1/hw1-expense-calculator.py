"""
Personal Finance Calculator
Student: Pavarun Promsuwicha
Date: 26/07/2025
Purpose: Calculate monthly budget and savings
"""

# Collect user inputs
print("=== MONTHLY BUDGET CALCULATOR ===")
monthly_income = float(input("Enter your monthly income(THB): ")) # Input float(decimal)
rent_cost = float(input("Enter your monthly rent/housing cost(THB): "))
food_budget = int(input("Enter your monthly food budget(THB): ")) # Input int(whole number)
transportation_cost = float(input("Enter your monthly transportation cost(THB): "))
entertainment_budget = int(input("Enter your monthly entertainment budget(THB): "))
emergency_fund_percent = float(input("Enter the percentage to save for emergency(e.g., 10.5): "))
investment_percent = float(input("Enter the percentage to invest(e.g., 15.0): "))
 
# Calculate total expenses
total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
remaining_income = monthly_income - total_expenses
emergency_fund_amount = (emergency_fund_percent / 100) * monthly_income
investment_amount = (investment_percent / 100) * monthly_income

# Calculate final savings
available_savings = remaining_income - emergency_fund_amount - investment_amount
expense_ratio = (total_expenses / monthly_income) * 100

# Display results
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund({emergency_fund_percent}%): {emergency_fund_amount:.2f} THB")
print(f"Investment({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")