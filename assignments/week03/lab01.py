# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

if 0 <= age <= 12 :
    print("Child")
elif 13 <= age <= 19 :
    print("Teenager")
elif 20 <= age <= 59 :
    print("Adult")
elif 60 <= age <= 150 :
    print("Senior")
else :
    print("Invalid")