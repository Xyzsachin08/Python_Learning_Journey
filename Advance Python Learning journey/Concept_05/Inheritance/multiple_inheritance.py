class Father:
    def money(self):
        print("Father gives money")

class Mother:
    def care(self):
        print("Mother gives care")

class Child(Father, Mother):
    def fun(self):
        print("Child enjoys")

c = Child()

c.money()
c.care()
c.fun()