class Parent:
    def papa(self):
        print("daddy's home")

class Child_1(Parent):
    def child_1(self):
        print("today is my bday")

class Child_2(Parent):
    def child_2(self):
        print("today is my brother bday")

p = Child_1()
p.child_1()
p.papa()

print("--------")

p1 = Child_2()
p1.child_2()
p1.papa()