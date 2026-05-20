class Grandfather:
    def land(self):
        print("Grandfather has land")

class Father(Grandfather):
    def house(self):
        print("Father has house")

class Son(Father):
    def bike(self):
        print("Son has bike")

s = Son()

s.land()
s.house()
s.bike()