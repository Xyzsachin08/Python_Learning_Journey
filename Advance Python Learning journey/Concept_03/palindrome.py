user_input = str(input("Enter a string"))
rev = ""
for i in user_input:
    rev = i + rev
    
if user_input == rev:
    print("Palindrome")
else:
    print("Not Palindrome")