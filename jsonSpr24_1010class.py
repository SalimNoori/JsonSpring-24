# Importing the 'json' module to work with JSON data.
import json

# Creating a dictionary named 'data' containing information about myself.
data = { 
    'name': 'John Doe',
    'age': 29, 
    'city': 'Washington, WA', 
    'interests': ['Traveling', 'Cricket', 'Soccer', 'Hiking', 'Studying'],
    'is_student': True 
}

# Creating a JSON and writing the Python object contents to the JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been written to data.json")
