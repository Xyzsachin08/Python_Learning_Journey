class Student:
    def __init__(self):
        self.__marks = 0

    # setter method
    def set_marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Invalid marks")

    # getter method
    def get_marks(self):
        return self.__marks


s = Student()

s.set_marks(90)

print(s.get_marks())