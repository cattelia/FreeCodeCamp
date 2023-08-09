#Serialization Format: Javascript Object Notation
#Aka - JSON
#"Discovered" by Douglas Crockford

import json

#JSON represented data as nested "dictionaries"
data = '''{

    "name" : "Joe",
    "phone" : {
        "type" : "intl",
        "number" : "1+ 123 456 7890"
    }, 
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data) #--> returns a dictionary
print(info)
print('Name: {}'.format(info["name"]))
print('Hide: {}\n'.format(info['email']['hide']))

'''

Notice how these use curly braces and have key:value pairs.
Everything in the ''' ''' is a string, which is fed into json.loads(str)
    and then returns us a dictionary assigned to "info"
    {'name': 'Joe', 'phone': {'type': 'intl', 'number': '1+ 123 456 7890'}, 'email': {'hide': 'yes'}}

'''

#JSON represents data as nested "lists"

input = '''[

    {
        "id" : "000",
        "x" : "i",
        "name" : "Joe"
    },
    {
        "id" : "011",
        "x" : "7",
        "name" : "Sara"
    }

]'''

info = json.loads(input)
print(info)
print("User count: {}".format(len(info)))
for item in info:
    print("Name: {}".format(item["name"]))
    print("ID: {}".format(item["id"]))
    print("Attribute: {}".format(item["x"]))


#PRACTICE: What will the following code print?
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])

#--> Mrugesh
