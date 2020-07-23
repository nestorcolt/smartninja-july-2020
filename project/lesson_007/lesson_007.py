import json

"""
    Resources:
        https://docs.python.org/3/library/json.html

"""

data = None

with open("people.json") as _file:
    data = json.load(_file)

"""
Save new JSON file from people.json as good_people.json with a better format

with open("good_people.json", "w") as writer:
    json.dump(data, writer, indent=4, separators=[",", ":"])

"""

# print each individual user (all data)
for user in data:
    print(user)

# print each individual user (first name and last name)
for user in data:
    print(user["first_name"] + " " + user["last_name"])
    print(user["email"] + " " + user["country"])
    print(" ")

##############################################################################################
