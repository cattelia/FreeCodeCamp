class Bank:



    def __init__(self, name, balance = 0, ledger=None):
        # Collect and assign the instance name, balance, and ledger
        #   self declared at initialization
        #   balance defaults to 0/Zero
        #   ledger defaults to dictionary object type
        self.name = name
        self.balance = balance
        if ledger is None:
            ledger = []
            self.ledger = ledger
     

    
  
    def __str__(self):
        # str.center(#Limit, fillChar)
        #   *************Food*************
        #   *************Cat**************
        ''' Fake self.ledger to reference 

        ledger = [
            '{"amount": 20, "description": this is more than characters}',
            #012345678901234567890123456789012345678
            '{"amount": 1, "description": grocery}',
            '{"amount": 1, "description": ""}'
        ]

        '''


        header = self.name.center(30, "*")
        print(header)

        for entry in self.ledger:
            # Find the end of amount and go until you find the first comma (,)
            amount_item = entry[entry.find('t": ') + 4:entry.find(",")]
            # Make it into a xx.00 number for formatting later using .2f in formatting by converting it to a float
            amount_item = "{:.2f}".format(float(amount_item))
            # Find the end of description and go until you find the close curly bracket (})
            description_item = entry[entry.find('n": ') + 4:entry.find("}")]
            print("{:<23}{:>7}".format(description_item[0:23], amount_item))

        return ''
    

    
  
    def deposit(self, amount, description = ""):
        # Add the monies to the balance counter using Bank.update_balance(). It will always be positive.
        # Make the entry using what deposit received, empty string if no description was given.
        # Append to self.ledger for access later
        # Update bank accounts
        ''' https://stackoverflow.com/questions/43768055/python-class-instance-variable-isolation '''

        entry = '{"amount": ' + str(amount) + ', "description": ' + description + '}'
        self.ledger.append(entry)

        print("Depositing ${:.2f} in {}".format(amount, self.name))
        self.update_balance(amount)
        return self.balance
    



    def withdraw(self, amount, description=""):
        # Check if there is enough in the bank versus how much we want to take out using Bank.check_funds()

        if self.check_funds(amount) == False:
            print("Insufficient funds")
            return False
        
        else:
            entry = '{"amount": ' + str(-amount) + ', "description": ' + description + '}'
            self.ledger.append(entry)

            print("Withdrawing ${:.2f} from {}".format(amount, self.name))
            self.update_balance(-amount)
            return True

  
    def transfer(self, amount, category):
        # Instance (self) to send money to another Bank instance (category) of a certain amount
        # Check that (self) has enough, if not return False
        # else transfer the amount to (category) and deduct the amount from balance

        if self.check_funds(amount) == False:
            print("Cannot transfer to {}".format(category.name))
            return False
        else:
            category.deposit(amount)
            self.withdraw(amount, "Transfer to {}".format(category.name))
            return True
        


    def check_funds(self, amount):
        # Define global variable within function
        # Check if there is enough in the bank versus how much we want to take out
        # If not enough in the Bank, return False if there is, return True
        # Called in Transfer() and Withdraw()
        
        if self.balance < amount:
            return False
        else:
            return True

    
  
    def get_balance(self):
        # Return the balance variable
        #print("${:.2f} in {}".format(self.balance, self.name))

        return self.balance
     

    
  
    def get_ledger(self):
        # Return the ledger
        # For debugging use
        print(self.ledger)
    

    
  
    def update_balance(self, amount):
            # If deposit() -> balance + amount
            # If withdraw() -> balance + (-amount)

        self.balance = self.balance + amount
        return self.balance
    

def create_spend_chart(categories=""):
    # Function outside of the class Bank
    '''
    In: List of categories
    Out: ASCII Chart representing how much was spent in each category based on percentage
    '''
    for i in range (100, -10, -10):
        print("{:>3}|".format(i))
    pass



'''
dog = Bank("Dog")
cat = Bank("Cat")
#food.get_balance()
dog.deposit(5, "Treats!")
dog.get_balance() #5
cat.get_balance() #0
print("")

dog.transfer(1, cat)
dog.get_balance()
cat.get_balance() #1
print("")

dog.transfer(5, cat)
dog.get_balance()
cat.get_balance() #1
print("")

#dog.get_ledger()
#cat.get_ledger()

dog.withdraw(1.50, "Puppychino")
dog.get_balance()
print("")

print(cat)
print(dog)
#entertainment = Bank("Entertainment")
'''

food = Bank("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
print("")

clothing = Bank("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(food.get_balance())
print(clothing.get_balance())
print("")

auto = Bank("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print("")

print(food)
print(clothing)
print(auto)

