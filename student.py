students = []

class Student:
    school_name = "Podstawowa"
    def __init__(self, name, student_id=332):
        self.name = name
        self.idStudent = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name