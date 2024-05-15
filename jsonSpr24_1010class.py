# Importing the 'json' module to work with JSON data.
import json
from msilib import add_data

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

#Opening the Json file for reading 
with open('data.json', 'r') as json_file: 
    #Create an object called loaded_data. Load the json file into the argument parameter. 
    loaded_data = json. load (json_file)



print("Sucessfully able to read data.json")
print(loaded_data)

#Altering the JSON object
loaded_data['age'] = 34 #<-ints 
loaded_data['interests'].append('Secret Hobby')

loaded_data['interests'].remove('Secret Hobby')


#Rewrite the changes to the Json file
with open('data.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)



