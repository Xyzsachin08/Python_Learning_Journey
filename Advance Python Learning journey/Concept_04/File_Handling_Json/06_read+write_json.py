import json

# Step 1: Python data
data = {
    "name": "Sachin",
    "age": 19
}

# Step 2: Convert to JSON
json_data = json.dumps(data)
print("JSON:", json_data)

# Step 3: Convert back to Python
python_data = json.loads(json_data)
print("Python:", python_data)