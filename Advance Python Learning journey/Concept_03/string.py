#String
s = "Sachin"

#Indexing
s = "Python"

print(s[0])   # P
print(s[3])   # h
print(s[-1])  # n

#Slicing
s = "Python"

print(s[0:3])   # Pyt
print(s[:4])    # Pyth
print(s[2:])    # thon
print(s[::-1])  # nohtyP (reverse)

#String Methods
s = "hello world"
s.upper()      # HELLO WORLD
s.lower()      # hello world
s.title()      # Hello World
s.capitalize() # Hello world




#Check method
s.isalpha()    # only letters?
s.isdigit()    # only numbers?
s.startswith("he")
s.endswith("ld")



#Search method
s.find("world")   # index
s.count("l")      # count



#Concatenation
a = "Hello"
b = "World"

print(a + " " + b)   # Hello World


#Formatting
name = "Sachin"
age = 19

print("My name is %s and age is %d" % (name, age))

#fromat() method
print("My name is {} and age is {}".format(name, age))

#f-string 
print(f"My name is {name} and age is {age}")
