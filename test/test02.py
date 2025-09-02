def check_age(age) :
    if 0 <= age < 13 :
        print("child")
    elif 13 <= age <= 19 :
        print("teen")
    elif 20 <= age <= 59 :
        print("adult")
    elif 60 <= age <= 120 :
        print("senior")
    else :
        print("invalid")

if __name__ == "__main__" :
    demo_age = [10, 16, 25, 65]
    for age in demo_age:
        check_age(age)