'''
# basic function
def greet():
    print("Hello")
    
greet()


#Function with return
def add(a, b):
    return a +b
result = add(45,78)
print(result)

#Built-in function

print("sachin")
print(len("Sachin"),type(10))


#User define function
def greet(name):
    return "Hello" + name

print(greet( name = " sachin"))

'''

#lamda function

add = lambda a, b: a + b
print(add(3, 4))