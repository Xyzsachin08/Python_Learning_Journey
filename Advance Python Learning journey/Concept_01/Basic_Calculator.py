"Take two numbers and operator (+, -, *, /) and perform operation."

num1 = int(input("Enter a number one: "))
num2 = int(input("Enter a number Two: "))


operator = input("Enter a operator(+ , -, *, /)")

if operator == "+":
    print(f"{num1} + {num2}", num1+num2)
elif operator == "-":
    print(f"{num1} - {num2}", num1-num2)
elif operator == "*":
    print(f"{num1} * {num2}", num1*num2)
elif operator == "/":
    print(f"{num1} / {num2}", num1/num2)
else:
    print("You not enter correct operator")
    
