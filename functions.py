students = []

def addStudent(name, idStudent=111):
    student = {name, idStudent}
    students.append(student)

def printStudents():
    print(students)

def show_args(name, **args):
    print(name)
    print(args["pattern1"], args["pattern2"])

def save_file(students):
    f = open("students.txt", "a")
    f.write(students + "\n")

def read_file():
    try:
        f = open("students.txt", "r")
        for line in f:
            student = f.readline()
            print("Imie {0}: ".format(student))
            addStudent(student)
    except FileExistsError:
        print("Brak pliku")

read_file()


print("Do you want to add user name Y/N")
answer = input(": ")

"""Zapis do pliku tylko w string"""

if answer.capitalize() == "Y":
    student_name = input("Insert the name of student: ")
    student_id = input("Insert the student id: ")
    addStudent(student_name, student_id)
    save_file(student_name)
else:
    print(students)

double = lambda x:x*2
master = lambda x:((x+2)*4)
print(double(4))
print(master(2))