class Student:
    def __init__(self):
        self.__marks = 0

    # getter
    @property
    def marks(self):
        return self.__marks

    # setter
    @marks.setter
    def marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Invalid marks")


s = Student()

s.marks = 90

print(s.marks)