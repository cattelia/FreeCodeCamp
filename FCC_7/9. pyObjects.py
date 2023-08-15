#Warning - this lecture is very much about definitions and mechanics of objects
#It is more about "how it works" and "terminology" vs "how to use it"

#__Data Structures__

inp = input("Europe floor?: ")
usf = int(inp) + 1
print("US floor {}\n".format(usf))

#Object Oriented
'''
- A program is made up of many cooperating objects
- Instead of being the "whole program" - each object is a little "island" within the program and cooperatively working with other objects
- A program is made up of one or more objects working together - objects make use of each other's capabilities
'''

#Object
'''
- An Object is a bit of self-contained Code and Data
- A key aspect is to break the problem into smaller parts (divide and conquer)
- Objects have boundaries that allow us to ignore un-needed detail
- We have been using OOP with: String Objects, Int Objects, Dict Objects, etc.
'''

#You can think of these are their own little bit of Code/Data as their own little programs with I/O themselves
# uppercase(), strip(), etc.

'''
Class - a template - Dog

Method or Message - A defined capability of a class - break()

Field or Attribute - A bit of data in a class - length

Object or Instance - A particular instance of a class - Lassie
'''

#Sample Class

#This is the template for making 'PartyAnimal' objects
class PartyAnimal:
    #Each 'PartyAnimal' object has a bit of data.
    x = 0

    #Each 'PartyAnimal' object has a bit of code. 
    def party(self):
        self.x += 1
        print("So far {}".format(self.x))

#Constructing a PartyAnimal object and store it in 'an'
an = PartyAnimal()

#Tell the object to run the party() code within it (The method)
an.party()  #Another way to think of this is:  PartyAnimal.party(an)
an.party()
an.party()

#Remember dir() and type()?
print(type(an)) #>>> <class '__main__.PartyAnimal'>
print(dir(an))  #>>> ['__class__', '__delattr__', ..., 'party', 'x'] Notice our party method and attribute/'x' is there.

#FreeCodeCamp Practice: What will print?
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

# 2
# 4