import json
##JSON TO PYTHON DICT
test_json = '{"python": "3.14.00", "OS": "Fedora44", "Linux": "7.00RC"}'
json_dict = json.loads(test_json)
print(json_dict["python"], json_dict["Linux"])

##PYTHON DICT TO JSON
json_value = json.dumps(json_dict)
print(json_value)

##LEGAL DATA TYPES
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, ))
print(json.dumps(x, indent=4, sort_keys=True))