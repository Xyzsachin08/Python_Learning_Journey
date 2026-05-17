'''
class Bank:
    def __init__(self):
        self.__balance = 5000
b = Bank()
print(b.__balance)   
#output = attribute error

'''
class Canara:
    def __init__(self):
        self.__paise = 100
        
    def show_paise(self):
        print(self.__paise)
        
s= Canara()
s.show_paise()