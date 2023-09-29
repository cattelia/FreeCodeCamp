global deposit_ledger
global withdraw_ledger
deposit_ledger = {}
withdraw_ledger = {}

class Bank:

    def __init__(self) -> None:
        print("I have made a bank account")

    def deposit(self, amount, description):
        pass

    def withdraw():
        pass

    def get_balance():
        pass

    def create_spend_chart(categories):
        '''
        In: List of categories
        Out: ASCII Chart representing how much was spent in each category
        '''
        for i in range (100, -10, -10):
            print("{:>3}|".format(i))
        pass

food = Bank()
