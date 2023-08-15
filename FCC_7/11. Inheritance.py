#Object Orientation and the idea of Inheritance
'''
- When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little code.
- Another form of store and reuse
- Write once - reuse many times
- The new class (child) has all the capabilities of the old class (parent) - then some more.
'''

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print("{} constructed".format(self.name))

    def party(self):
        self.x = self.x + 1
        print("{} counts {}".format(self.name, self.x))

class Football(PartyAnimal):    #Inherits PartyAnimal()
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print("{} points {}".format(self.name, self.points))

s = PartyAnimal("Sara")
s.party()
#s has: x and party() but NOT touchdown()
j = Football("Joseph")
j.party()
j.touchdown()
#j has: x, party() AND touchdown()

#Review the terminology
'''
Class - a template >>> PartyAnimal
Attribute - A variable within a class >>> x
Method - A function within a class >>> party() || touchdown()
Object - A particular instance of a class >>> s || j
Constructor - Code that runs when an object is created >>> __init__()
Inheritance - The ability to extend a class to make a new class
'''

#FreeCodeCamp Practice: What is inheritance in OOP?
#>>> The ability to create a new class by extending an existing class.
