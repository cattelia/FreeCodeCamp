import json


#Simple Example 1
#Dictionary

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print("Name: {}".format(info["name"]))
print("Hide: {}\n".format(info["email"]["hide"]))

#Simple Example 2
#Lists

input = '''
[
    {
    "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {
    "id" : "010",
    "x" : "8",
    "name" : "Sam"
    }
]'''

info = json.loads(input)
print("User count: {}\n".format(len(info)))

for item in info:
    print("Name: {}".format(item["name"]))
    print("id: {}".format(item["id"]))
    print("Attribute: {}\n".format(item["x"]))