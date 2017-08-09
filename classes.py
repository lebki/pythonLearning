students = []
class Student:
    school_name = "Podstawowa"
    """
        Tak robi się komentarze wieloliniowe
        1
        2
        3
        4
        :param  
        :param
    """
    def __init__(self, name, idStudent=332):
        self.name = name
        self.idStudent = idStudent
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class HighSchoolStudent(Student):  # rozszerzenie jako parametr nowej klasy
    school_name = "Wyższa"

    def get_school_name(self):
        return "This is the highschool student"

    def get_name_capitalize(self):  # rozszerzenie z wykorzystaniem funkcji bazowej
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

print(Student.school_name)  # nie zalezy od instancji
janek = Student("Janek")
james = HighSchoolStudent("James")
print(james.get_name_capitalize())
print(james.get_school_name())
print(janek)
print(janek.get_school_name())