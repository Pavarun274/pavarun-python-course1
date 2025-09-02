# Exercise 2: Shopping Receipt
print("\n=== Shopping Receipt ===")
# Ask the user for:
# - Item name
# - Item price
# - Quantity
# Calculate and display the total cost

# Write your solution here:

silo = {}

item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
quentity = int(input("Enter quentity: "))

total = item_price * quentity

print()