# List and dictionaries - data structures
##############################################################################################
"""

    Resources:
        https://www.w3schools.com/python/python_ref_list.asp

"""

# Primitives data types

some_num = 4  # integer (whole number)
some_decimal = 3.14  # float (decimal number)
some_str = "Hello, SmartNinja!"  # string
human = True  # boolean (either True or False)

# Arrays (Lists in Python) - Data structure
some_list = [1, 34, 12, 17, 87]
# print(some_list)

another_list = ["tesla", "toyota", "nissan"]
# print(another_list)

mixed_list = [22, "elon", True, "SmartNinja", 3.14]
# print(mixed_list)

# Iterating over a list
for item in mixed_list:
    # print(item)
    pass

# Indexing
element = mixed_list[4]
# print(element)

# negative indexing
element = mixed_list[-5]
# print(element)

# slicing
elements = mixed_list[0:-2]
# print(elements)

# list methods

# append
new_list = []

new_list.append(2)
new_list.append(True)
new_list.append(False)
new_list.append("kaka")
# print(new_list)

# remove
new_list.remove(True)
# print(new_list)


# pop
pop_element = new_list.pop(0)
# print(pop_element)

# count
counter = new_list.count(False)
# print(counter)

# --------------
# List length
mixed_list = [22, "elon", True, "SmartNinja", 3.14]
# print(len(mixed_list))

##############################################################################################
# Dictionaries
box = {"height": 20, "width": 45, "length": 30, 2: "kaka"}

# Referencing a element in a dictionary
element = box["width"]
# print(element)

# get method
element_1 = box.get("height", None)  # exist
element_2 = box.get("Heights", None)  # no exist
# print(element_1)
# print(element_2)

# dictionary keys
keys = box.keys()
# print(keys)

# dictionary values
values = box.values()
# print(values)

# dictionary items
items = box.items()
# print(items)


# Iterating over a dictionary
for key, value in box.items():
    # print(key, value)
    pass

##############################################################################################
