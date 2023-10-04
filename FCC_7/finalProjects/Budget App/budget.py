class Bank:


    def __init__(self, name, balance=0, ledger={}) -> None:
        # Collect and assign the instance name, balance, and ledger
        self.name = name
        self.balance = balance
        self.ledger = ledger
        #self.transfer = transfer(self)

    '''
    def __str__(self):
        # str.center(#Limit, fillChar)
        #   *************Food*************
        #   *************Cat**************
        #   Still need the rest of the ledger (This could potentially print to a log?)
        header = self.name.center(30, "*")
        return header
    '''

    def deposit(self, amount, description=""):
        # Add the monies to the balance counter using Bank.update_balance(). It will always be positive.
        ''' Still need to append {description: amount} to the transaction_ledger '''

        print("Depositing ${}.00 in {}".format(amount, self.name))
        self.update_balance(amount)


    def withdraw(self, amount, description=""):
        # Check if there is enough in the bank versus how much we want to take out using Bank.check_funds()
        ''' Still need to include this in the ledger when we print the Class instance '''

        if self.check_funds(amount) == False:
            print("Insufficient funds")
            return False
        else:
            print("Withdrawing ${}.00 from ${}.00".format(amount, self.balance))
            self.update_balance(-amount)
            return True



    def get_balance(self):
        # Return the balance variable

        print("${}.00 in {}".format(self.balance, self.name))
        return self.balance




    def transfer(self, amount, category):

        if self.check_funds(amount) == False:
            print("Cannot transfer to {}".format(category))
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

        False if self.balance < amount else True

        '''
        if balance < amount:
            return False
        else:
            return True
        '''

        



    def update_balance(self, amount):
            # If deposit() -> balance + amount
            # If withdraw() -> balance + (-amount)

        self.balance = self.balance + amount
        return self.balance


def create_spend_chart(categories):
    '''
    In: List of categories
    Out: ASCII Chart representing how much was spent in each category based on percentage
    '''
    for i in range (100, -10, -10):
        print("{:>3}|".format(i))
    pass



dog = Bank("Dog")
#food.get_balance()
dog.deposit(5)
dog.get_balance() #5
print("")
cat = Bank("Cat")
cat.get_balance() #0
print("")
dog.transfer(1, cat)
cat.get_balance() #1
dog.get_balance()
dog.transfer(5, cat)
print("")
cat.get_balance() #1
dog.get_balance()
#dog.transfer(10, cat)

'''
Current Log: NEED TO FIX WITHDRAW?/TRANSFER?/CHECK_FUNDS?

Depositing $5.00 in Dog
$5.00 in Dog

$0.00 in Cat

Depositing $1.00 in Cat
Withdrawing $1.00 from $5.00
$1.00 in Cat
$4.00 in Dog
Depositing $5.00 in Cat
Withdrawing $5.00 from $4.00

$6.00 in Cat
$-1.00 in Dog
'''
