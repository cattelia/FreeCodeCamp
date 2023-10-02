
################################################################

class Test:
    global balance
    balance = 0
   
    def __init__(self):
        print("Hello")
   
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
        if balance < amount:
            print("There is not enough in the bank")
            return False
        else:
            Test.update_balance(-amount)
            return True
   
    def show_balance(self):
        print(balance)
   
a = Test()
a.show_balance()
a.func1(10)
a.show_balance()

################################################################

'''

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

################################################################

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