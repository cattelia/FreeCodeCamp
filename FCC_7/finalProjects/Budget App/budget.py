global deposit_ledger
global withdraw_ledger
deposit_ledger = {}
withdraw_ledger = {}

class Bank:


    def __init__(self) -> None:
        print("I have made a new bank account")

    def deposit(self, amount, description=""):
        pass

    def withdraw(self, amount, description=""):
        pass

    def get_balance(self):
        pass

    def transfer(self):
        pass

    def check_funds(self):
        pass


def create_spend_chart(categories):
    '''
    In: List of categories
    Out: ASCII Chart representing how much was spent in each category based on percentage
    '''
    for i in range (100, -10, -10):
        print("{:>3}|".format(i))
    pass

food = Bank()
food.withdraw(100)
food.withdraw(12)
entertainment = Bank()
entertainment.withdraw(1000)
