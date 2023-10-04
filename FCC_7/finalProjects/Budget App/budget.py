class Bank:


    def __init__(self, name, balance=0, ledger={}):
        # Collect and assign the instance name, balance, and ledger
        #   self declared at initialization
        #   balance defaults to 0/Zero
        #   ledger defaults to dictionary object type
        self.name = name
        self.balance = balance
        self.ledger = ledger


    def __str__(self):
        # str.center(#Limit, fillChar)
        #   *************Food*************
        #   *************Cat**************
        ''' Still need the rest of the ledger (This could potentially print to a log?) '''
        ''' Dont start working on until ledger is working '''

        header = self.name.center(30, "*")
        return header


    def deposit(self, amount, description=""):
        # Add the monies to the balance counter using Bank.update_balance(). It will always be positive.
        ''' Still need to append {description: amount} to the ledger '''

        print("Depositing ${}.00 in {}".format(amount, self.name))
        self.update_balance(amount)


    def withdraw(self, amount, description=""):
        # Check if there is enough in the bank versus how much we want to take out using Bank.check_funds()
        ''' Still need to append {description: amount} to the ledger '''

        if self.check_funds(amount) == False:
            print("Insufficient funds")
            return False
        else:
            print("Withdrawing ${}.00 from {}".format(amount, self.name))
            self.update_balance(-amount)
            return True



    def get_balance(self):
        # Return the balance variable

        print("${}.00 in {}".format(self.balance, self.name))
        return self.balance



    def transfer(self, amount, category):
        # Instance (self) to send money to another Bank instance (category) of a certain amount
        # Check that (self) has enough, if not return False
        # else transfer the amount to (category) and deduct the amount from balance
        ''' Still need ot include this in the ledger for both (self) and (category) '''

        if self.check_funds(amount) == False:
            print("Cannot transfer to {}".format(category.name))
            return False
        else:
            category.deposit(amount)
            self.withdraw(amount)
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



dog = Bank("Dog")
cat = Bank("Cat")
#food.get_balance()
dog.deposit(5)
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

#entertainment = Bank("Entertainment")