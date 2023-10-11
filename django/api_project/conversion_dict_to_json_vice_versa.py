import json

m = {'name':'ameya'}
print("value of m:",m)
print("type of m:",type(m))

print(":converting dictionary to JSON")
json_data = json.dumps(m)
print(json_data)
print("Type of json_data:",type(json_data))

print("Convert JSON to dictionary")
dict_convert = json.loads(json_data)
print(dict_convert)
print("data type:",type(dict_convert))

