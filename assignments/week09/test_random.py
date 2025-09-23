import random

def test_random():
    # สร้างตัวแปร random_number ตัวแปรคือการสุ่มเลขระหว่าง 1-10
    random_number = random.randint(1, 10)
    return random_number

num = test_random()
while True:
    num_user = int(input("Enter your guess number(1-10): "))
    if num_user == num:
        print("Congrats!")
        break
    elif num_user > num:
        print("Too high")
    elif num_user < num:
        print("Too low")