#Without super()
'''
class Father:

    def __init__(self):
        print("Father constructor")

class Son(Father):

    def __init__(self):
        print("Son constructor")

s = Son()


#Using super()

class Father:

    def __init__(self):
        print("Father constructor")

class Son(Father):

    def __init__(self):
        super().__init__()
        print("Son constructor")

s = Son()

'''

#Real life example
class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

s = Student("Sachin", 85)

print(s.name)
print(s.marks)