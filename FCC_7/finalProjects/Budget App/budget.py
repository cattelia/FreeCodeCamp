class Bank:
        # Initialize global variables
    global balance
    balance = 0

    global transaction_ledger
    transaction_ledger = {}


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
        Bank.update_balance(amount)
        pass


    def withdraw(self, amount, description=""):
        # Check if there is enough in the bank versus how much we want to take out using Bank.check_funds()
        ''' Still need to include this in the log when we print the Class instance '''

        if Bank.check_funds(amount) == False:
            print("There is not enough to cover ${}.00".format(amount))
        else:
            print("Withdrawing -${}.00".format(amount))



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
        # Called in Deposit() and Withdraw()
        ''' This is incomplete - this will work for Withdraw but not Deposit'''

        global balance

        if balance < amount:
            return False
        else:
            Bank.update_balance(-amount)
            return True


    @staticmethod
    def update_balance(amount, add=balance):
            # If deposit(), amount
            # If withdraw(), -amount
        global balance
        balance = add + amount
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
food.get_balance()
print(food)
cat = Bank("Cat")
print(cat)