dict1 = {"name": "John", "age": 25, "city": "New York"}
dict2 = {"name": "Jane", "age": 30, "city": "Los Angeles"}
dict3 = {"name": "Bob", "age": 40, "city": "San Francisco"}
dict4 = {"name": "Alice", "age": 35, "city": "Seattle"}

print(dict1.items())
print(dict2.keys())
print(dict3.values())
print(dict4["age"])
print(dict4.get("city"))

dict1.update(dict3)
print(dict1)

dict1.clear()
dict_copy = dict2.copy()
age = dict3.pop("age")
item = dict4.popitem()

# This code creates a new dictionary called new_dict with keys "name", "age", and "city", and values "Unknown", 0, and None, respectively.
new_dict = dict.fromkeys(["name", "age", "city"], "Unknown")
new_dict["age"] = 0
new_dict["city"] = None

print(dict1)
print(dict_copy)
print(age)
print(item)
print(new_dict)