"Swap two numbers without using third variable."

a = 10
b = 20

a,b = b,a
print("a = ", a)
print("b = ", b)



#using Third Variable

c = a
a = b
b = c

print("a =",a)
print("b =",b)