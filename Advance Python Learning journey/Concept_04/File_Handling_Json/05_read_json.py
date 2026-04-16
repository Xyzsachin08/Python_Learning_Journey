import json
with open("material.json","r") as file:
    material = json.load(file)
    
print(material)