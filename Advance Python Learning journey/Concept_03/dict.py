student = {
    "name": "Sachin",
    "age": 19,
    "branch": "Engineering"
}
'''
#Access Value
print(student["name"])   
print(student["age"])    


#using get
print(student.get("name"))


#Add / Update Values
student["age"] = 20          # update
student["city"] = "Pune"     #add new

print(student["city"])   # "pune"
print(student["age"])    # 20


#Remove Elements
student.pop("age")     # remove key
del student["name"]    # delete
student.clear()        # empty dictionary
'''

#Iteration through keys
for key in student:
    print(key)
    
    
#Iteration through value
for value in student.values():
    print(value)
    

#Loop through values
for k, v in student.items():
    print(k, v)
    
#nested_dictionary

student = {
    "s1" : {"name":"sachin", "age": 19},
    "s2":{"name":"Rahul","age":20}
}

print(student["s1"]["name"])



#Dictionary methods
student.keys()      # all keys
student.values()    # all values
student.items()     # key-value pairs
student.update({"age": 21})



#Dictionary Comprehension
sq = { x : x*x for x in range(5)}
print(sq)

