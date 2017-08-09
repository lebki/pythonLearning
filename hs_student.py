from student import *

class HighSchoolStudent(Student):  # rozszerzenie jako parametr nowej klasy
    school_name = "Wyższa"

    def get_school_name(self):
        return "This is the highschool student"

    def get_name_capitalize(self):  # rozszerzenie z wykorzystaniem funkcji bazowej
        original_value = super().get_name_capitalize()
        return original_value + "-HS"