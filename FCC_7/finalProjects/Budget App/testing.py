################################################################################################################################

class Test:
    global balance
    balance = 0
   
    def __init__(self, name):
        #Collect and assign the instance name
        self.name = name
    

    def __str__(self) -> str:
        #return self.__class__.__name__ FAILED >>> This returned the class Name
        #header = "*************{}*************".format(self.name) FAILED >>> this did not take into account the maximum length of characters allowed.
        header = self.name.center(30, "*")
        return header


    @staticmethod
    def update_balance(amount, add=balance):
        #If from func1 (deposit), amount
        #if from func2 (withdraw), -amount

        global balance
        balance = add + amount
        return balance
    
   
    def func1(self, amount):
        #acting like deposit

        Test.update_balance(amount)
        print("You deposited {} amount".format(amount))

   
    def func2(self, amount):
        #acting like withdraw

        global balance
        if balance < amount:
            print("There is not enough in the bank")
            return False
        else:
            Test.update_balance(-amount)
            return True
   

    def show_balance(self):
        print(balance)


    def check_funds(self, amount):
        # Define global variable within function
        # Check if there is enough in the bank versus how much we want to take out
        # If not enough in the Bank, return False if there is, return True
        # THIS IS CALLED AND CHECKED IN DEPOSIT() AND WITHDRAWAL()
        global balance

        if balance < amount:
            print("There is not enough to cover ${}.00".format(amount))
            return False
        else:
            Test.update_balance(-amount)
            return True

'''  
a = Test("Food")
a.show_balance()
a.func1(10)
a.show_balance() 
print(a)
'''

################################################################################################################################

#REGEX: https://www.py4e.com/html3/11-regex
#String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods
#https://regex101.com/r/gT6vU5/127

import re


class Test:

    def __init__(self, name, balance=0, ledger=[]):
        self.name = name
        self.balance = balance
        self.ledger = ledger

    def __str__(self):
        # ['{"amount": 2, "description": cat food}', '{"amount": 1, "description": grocery}']
        header = self.name.center(30, "*")
        for item in self.ledger:
            pass
        return ""

    def deposit(self, amount, description=""):
        entry = '{"amount": ' + str(
            amount) + ', "description": ' + description + '}'
        self.balance += amount
        self.ledger.append(entry)
        return self.balance, self.ledger

    def get_ledger(self):
        print(self.ledger)

    def get_balance(self):
        print("Balance:", self.balance)


test = Test("Test")
test.deposit(2, "cat food")
test.deposit(1, "grocery")
#test.get_ledger()
#test.get_balance()
#print(test)

line = 'X-Sieve: CMU Sieve 2.3'

#re.find('^X.*:')
'''
line = 'X-Sieve: CMU Sieve 2.3'

Methods:
re.search()
re.findall()
re.find()
re.startswith()

Expressions:
^ - Match the start of a line, '^X'
. - Match any character (Singular match case) '^X.'
* - Many times (Many times)
\S - Match any non-whitespace cahracter
\s - Match only whitespace characters
+ - One or more times
'''
'''
pattern = re.compile("^Cat")
pattern.search(str)
'''
'''
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
'''

ledger = [
    '{"amount": 20, "description": this is more than characters}',
    #012345678901234567890123456789012345678
    '{"amount": 1, "description": grocery}',
    '{"amount": 1, "description": ""}'
]


def search(ledger):
    header = "Cat".center(30, "*")
    print(header)

    for entry in ledger:

        #line = entry.split(",")
        #amount = entry[1:entry.find(",")]
        amount_item = entry[entry.find('t": ')+4:entry.find(",")]
        description_item = entry[entry.find('n": ')+4:entry.find("}")]
        amount_item = "{}.00".format(amount_item)
        print("{:<20}{:>10}".format(description_item[0:20], amount_item))
        

        
        for item in line:
            item = item.replace("{", "").strip()
            item = item.replace("}", "")
            prefix = "amount:" if item.startswith(
                '{"amo') == True else "description:"


'''
['{"amount": 2', ' "description": cat food}']      #list
Item: {"amount": 2                                 #str
Item:  "description": cat food}                    #str

['{"amount": 1', ' "description": grocery}']       #list
Item: {"amount": 1                                 #str
Item:  "description": grocery}                     #str
'''




'''
search(ledger)

if line.startswith('test:'):
    print(line[5:line.find('.')])

    
import re

class Test:

    def __init__(self, name, balance=0, ledger=[]):
        self.name = name
        self.balance = balance
        self.ledger = ledger

    def __str__(self):
        # ['{"amount": 2, "description": cat food}', '{"amount": 1, "description": grocery}', ...]
        line = []
        header = self.name.center(30, "*")
        for item in self.ledger:
            line.append(item)
            # [ ' { " amount " : 2 , " description " : cat food } ' , 
            #   ' { " amount " : 1 , " description " : grocery } ' ]

        for i in line:
            i = i.split(",")
            # Item 1:
            # [ ' { " amount " : 2 ' , 
            #   ' " description " : cat food } ' ]
            # Item 2:
            # [ ' { " amount " : 1 ' , 
            #   ' " description " : grocery } ' ]
            i = i.split(":")
            print(i)


        return ""

    def deposit(self, amount, description=""):
        entry = '{"amount": ' + str(
            amount) + ', "description": ' + description + '}'
        self.balance += amount
        self.ledger.append(entry)
        return self.balance, self.ledger

    def get_ledger(self):
        print(self.ledger)

    def get_balance(self):
        print("Balance:", self.balance)


    def clear(self):
        self.balance = 0
        self.ledger = []
        return self.balance, self.ledger

test = Test("Test")

test.deposit(2, "cat food")
test.deposit(1, "grocery")
#test.get_ledger()
#test.get_balance()
print(test)


pledge = {}
print("Pledge:", pledge) #Pledge: {}
description = ""
amount = 1
pledge[description] = amount
print(pledge) #{'': 1}

pledge = {}

def update_dict(amount, description=""):
    pledge[description] =  amount
    print(pledge)

update_dict(1)              #{'': 1}
update_dict(2, "groceries") #{'': 1, 'groceries': 2
update_dict(2)              #{'': 2, 'groceries': 2} Overwrote: ''
'''


'''
balance = 10
amount = 10

def check_funds(amount):

    print("Balance: {}\nAmount: {}".format(balance, amount))

    #False if cache < balance else True
    if amount < balance:
        return False
    else:
        return True

print(check_funds(amount))


#>>>Calling the name of the Class<<<
class fruit:

    def __init__(self, fruit):
        self.fruit = fruit

a = fruit("peach")
print(a.__class__)
print(a.__class__.__name__)
print(type(a).__name__)



deposit_ledger = {}
withdraw_ledger = {}

def percentageMap(amount, description=""):


    for i in range(100, -10, -10):
        line = "{:>3}|".format(i)
        print(line)


def deposit(amount, description=""):
     #dictionary_name['key'].append(['value1'])

    deposit_ledger.setdefault("amount", []).append(amount)
    deposit_ledger["description"] = description
    deposit_ledger["description"].append("dog")
    return deposit_ledger
       
def withdraw(amount, description=""):
    amount = -amount
    print(amount)
   
#print(deposit(amount, description))
#print(withdraw(amount, description))

percentageMap(1000, "kitty")


#########Websites to Help#########

Dictionary assignments:
https://stackoverflow.com/questions/18263246/python-class-variable-update-based-on-dictionary?rq=3
Setattr(object, name, value)
https://docs.python.org/3/library/functions.html#setattr


class Test:

    def setVar(self, var):
        for key, value in var.items():
            withdraw = setattr(self, key, value)
        print(withdraw)

var = {"desc":10}
food = Test()
food.setVar(var)
'''

################################################################################################################################

'''
    def __init__(self):
        print("Starting the test")
        #self.A = 1
        #self.B = 2
   
    def withdraw(self, amount):
        pass
       
obj = Test()
print(obj.__dict__)
obj.withdraw(12, "food")

#Example Code
class A(object):  
    def __init__(self):  
        self.A=1  
        self.B=2  
obj=A()  
print(obj.__dict__)

#https://www.geeksforgeeks.org/python-call-function-from-another-function/
#https://www.sanfoundry.com/python-program-form-dictionary-object-class/
#https://www.programiz.com/python-programming/methods/built-in/staticmethod
#https://www.studymite.com/python/how-to-fix-unbound-local-errors-in-python
'''