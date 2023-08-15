#Object Lifecycle
'''
- Obj are created, used, and discarded
- We have special blocks of code (methods) that get called
    - At the moment of creation : constructor
    - At the moment of destruction : destructor
- Constructors are used a lot
- Destructors are used rarely
'''

class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1
        print("Count {}".format(self.x))

    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42 
print("an contains {}".format(an))
print("")
#Many Instances:
'''
- We can create lots of objects - the class template
- We can store each distinct object in its own variable
- We call this having multiple instances of the same class
- Each instance has its own copy of the instance variables
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

s = PartyAnimal("Sara") #"Sara" is z and assign this to the variable "s"
s.party()
print("")
j = PartyAnimal("Joseph") #"Joseph" is z and assign this to the variable "j"
j.party()
s.party()


#FreeCodeCamp Practice: What will print?
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

'''
Quincy constructed
Miya constructed
Quincy party count 1
Miya party count 1
Quincy party count 2
'''