
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Pavarun Promsuwicha", 19, "Rayong", "Thailand")  # name, age, city, country
    hobbies = []
    
    print("*" * 45)
    print("\tPersonal Information Manager")
    print("*" * 45)

    # Your code here

    while True:
        choice = input("Please select (1 disply, 2 add hobby, 3 remove hobby, 4 change age, 5 exit): ")

        if choice == "1":
            name, age, city, country = person
            print(f"Name: {name} \nAge: {age} \nCity: {city} \nCountry: {country}")
            print(f"Hobbies: {hobbies}")

        elif choice == "2":
            new_hobbies = input("Enter your new hobbies: ")
            hobbies.append(new_hobbies)
            print(f"Hobbies: {hobbies}")

        elif choice == "3":
            remove_hobbies = input("Enter hobby is you want to remove: ")
            hobbies.remove(remove_hobbies)
            print(f"Hobbies: {hobbies}")

        elif choice == "4":
            person_list = list(person)
            age = int(input("Enter your age: "))
            person_list[1] = age
            person = tuple(person_list)
            print(f"Name: {name} \nAge: {age} \nCity: {city} \nCountry: {country}")

        elif choice == "5":
            print("Thank you for using!")
            break

        else:
            print("Invalid")

    pass

if __name__ == "__main__":
    personal_info_manager()