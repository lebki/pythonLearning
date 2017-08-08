students = []

def addStudent(name, idStudent):
    student = {name, idStudent}
    students.append(student)

def printStudents():
    print(students)

def show_args(name, **args):
    print(name)
    print(args["pattern1"], args["pattern2"])

def save_file(students):
    f = open("students.txt", "a")
    f.write(students)

print("Do you want to add user name Y/N")
answer = input(": ")

"""Zapis do pliku tylko w string"""

if answer.capitalize() == "Y":
    student_name = input("Insert the name of student:")
    student_id = input("Insert the student id")
    addStudent(student_name, student_id)
    save_file(student_name)
else:
    print(students)