class Bank:
        # Initialize global variables
    global balance, ledger
    balance = 0
    ledger = {}


    def __init__(self, name) -> None:
        # Collect and assign the instance name
        self.name = name


    def __str__(self):
        # str.center(#Limit, fillChar)
        #   *************Food*************
        #   *************Cat**************
        ''' Still need the rest of the ledger (This could potentially print to a log?)'''
        header = self.name.center(30, "*")
        return header


    def deposit(self, amount, description=""):
        # Add the monies to the global balance counter using Bank.update_balance(). It will always be positive.
        ''' Still need to append {description: amount} to the transaction_ledger '''

        Bank.check_funds(amount)
        print("Depositing ${}.00".format(amount))
        Bank.update_balance(amount)


    def withdraw(self, amount, description=""):
        # Check if there is enough in the bank versus how much we want to take out using Bank.check_funds()
        ''' Still need to include this in the ledger when we print the Class instance '''

        if Bank.check_funds(-amount) == False:
            print("Insufficient funds. Balance: ${}.00\nYou are trying to withdraw ${}.00".format(balance, amount))
            return False
        else:
            print("Withdrawing ${}.00".format(amount))
            return True



    def get_balance(self):
        # Return the global balance variable

        print("${}.00".format(balance))
        return balance


    def transfer(self):
        pass


    @staticmethod
    def check_funds(amount):
        # Define global variable within function
        # Check if there is enough in the bank versus how much we want to take out
        # If not enough in the Bank, return False if there is, return True
        # Called in Transfer() and Withdraw()

        global balance
        cache = amount + balance

        #False if cache < balance else True
        if cache <= balance:
            return False
        else:
            return True

        


    @staticmethod
    def update_balance(amount):
            # If deposit(), amount
            # If withdraw(), -amount
        global balance
        print("Current ${}".format(balance))

        #cache = add + amount
        #print("Cache ", cache)
        #balance = cache

        print("Updated ${}".format(balance))
        return balance


def create_spend_chart(categories):
    '''
    In: List of categories
    Out: ASCII Chart representing how much was spent in each category based on percentage
    '''
    for i in range (100, -10, -10):
        print("{:>3}|".format(i))
    pass

food = Bank("Food")
#food.get_balance()
print(balance) #0

food.deposit(10) #10
#food.deposit(1) #11
print(balance) #10