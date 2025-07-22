# Complete this ATM simulation
balance = 1000
pin = "1234"

print("*" * 30)
print("\tATM simulation")
print("*" * 30)

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option (1-4): ")
        
        # Complete the menu logic here
        # Your code here:

        if choice == "1":
            print(f"Your balance is {balance}")

        elif choice == "2":
            withdraw = float(input("The amount of money you want to withdraw: "))
            if 0 <= withdraw <= balance:
                balance = balance - withdraw
                print(f"Successfully!!\nYour new balance is {balance}")
            elif withdraw < 0:
                print(f"Cannot withdraw negative balance.\nYour balance is {balance}")
            else:
                print(f"Cannot withdraw more than the amount available.\nYour balance is {balance}")

        elif choice == "3":
            deposit = float(input("The amount of money to be deposited: "))
            if deposit > 0:
                balance = balance + deposit
                print(f"Successfully!!\nYour new balance is {balance}")
            else:
                print(f"Cannot deposit negative balance.\nYour balance is {balance}")

        elif choice == "4":
            print("Thank you for using our service.")
            break

        else:
            print("Invalid choice! Please enter 1-4.")

else:
    print("Invalid PIN")
