class Bank:
    def __init__(self):
        self.__balance = 5000
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    
    def show(self):
        print(self.__balance)
        
b = Bank()
b.deposit(2000)
b.show()
# now we can easily control the invalid operation