"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

passing_grade = 50

def input_students(num_students = 0):
    """ students = [
        {}, {}
    ]
    for std in range(num_students):
        students['name'] = input(f"Enter name student {std + 1}: ")
        students['scores'] = int(input(f"Enter scores student {std + 1}: "))
    """
    students = [
        {
            'name': 'Pavarun',
            'scores': [78, 67, 88]
        },
        {
            'name': 'Supawit',
            'scores': [70, 80, 90]
        }
    ] # Member in this list is dictionaries
    return students

def calculate_averages(students):
    for student in students: # Loop = Member of students in above
        sum = 0
        for score in student['scores']:
            sum += score
        student['average'] = sum / len(student['scores'])
    return students

def display_results(students):
    for student in students:
        print("Name: ", student['name'])
        print("Average: %.2f" % student['average'])
        if student['average'] > passing_grade:
            print("Status: PASS")
        else:
            print("FAIL")

student_list = input_students()
student_list = calculate_averages(student_list)
display_results(student_list)

# num = input("Enter num of student: ")
# input_students(num)