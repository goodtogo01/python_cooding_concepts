import json

# todo Exercise 1: Convert the following dictionary into JSON format
from json import JSONEncoder
from json import JSONDecoder

from modifiers.AccessModifires_Default import obj

print('Exercise 1: Convert the following dictionary into JSON format')
data = {"key1": "value1", "key2": "value2"}
print("Original file : ", data)
print("With Json format : ", json.dumps(data, indent=4))

# todo Exercise 2: Access the value of key2 from the following JSON
print('\nExercise 2: Access the value of key2 from the following JSON')
sample_data = """{"key1" : "value1", "key2" : "value2"}"""
data = json.loads(sample_data)
print("Desire value fo Key2 is :", data['key2'])

# todo Exercise 3: PrettyPrint following JSON data
print('\nExercise 3: PrettyPrint following JSON data')
sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}
print("Pretty Print : ", json.dumps(sampleJson, indent=4))
# todo Exercise 4: Sort JSON keys in and write them into a file
print('\nExercise 4: Sort JSON keys in and write them into a file')
sampleJson = {"id": 1, "name": "value2", "age": 29}
print('Original file : ', sampleJson)
print(json.dumps(sampleJson, indent=4, sort_keys=True))
print('Done writing with json data into a file')

# todo Exercise 5: Access the nested key ‘salary’ from the following JSON
print('\Exercise 5: Access the nested key ‘salary’ from the following JSON')
sampleJson2 = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson2)
print(data['company']['employee']['payble']['salary'])
# todo Exercise 6: Convert the following Vehicle Object into JSON
print('\nExercise 6: Convert the following Vehicle Object into JSON')


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

    def dis(self):
        print("Original Data: ")
        print("Brand: ", self.name, "\nEngine :", self.engine, "\nPrice :", self.price)


vehicle = Vehicle("Honda CRV EX-L", "3.5L", 25811)
vehicle.dis()


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print("\nConvert into JSON formate : ", vehicleJson)

# todo Exercise 7: Convert the following JSON into Vehicle Object
print('\nExercise 7: Convert the following JSON into Vehicle Object')
#
#
# class Vehicle2:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
#
# def vehicleDecoder(obj):
#     return Vehicle2(obj['name'], obj['engine'], obj['price'])
#
#
# vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }')
# print(type(vehicleObj))
# print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

# todo Exercise 8: Check whether following json is valid or invalid. If Invalid correct it
print('\nExercise 8: Check whether following json is valid or invalid. If Invalid correct it')


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


invalidJsonData = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}"""
isValid = validateJSON(invalidJsonData)
print("Given JSON String is Valid : ", isValid)

# todo Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
print('\nExercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array')
jsonData = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"]
   },
   { 
      "id":2,
      "name":"name2",
      "color":["pink","yellow"]
   },
   {
   "name":"name5"
   }
]"""
data = json.loads(jsonData)
print(json.dumps(data, indent=4))

dataList = [item.get('name') for item in data]
print(dataList)