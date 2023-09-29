def percentageMap(amount, description=""):
    deposit_ledger = {}
    withdraw_ledger = {}
   
    for i in range(100, -10, -10):
        line = "{:>3}|".format(i)
        print(line)
       
    def deposit(amount, description):
        #dictionary_name['key'].append(['value1'])

        deposit_ledger.setdefault("amount", []).append(amount)
        deposit_ledger["description"] = description
        deposit_ledger["description"].append("dog")
        return deposit_ledger
       
       
    def withdraw(amount, description):
        withdraw_ledger.setdefault("amount", []).append(-amount)
        #withdraw_ledger["amount"] = -amount
        #withdraw_ledger["description"] = description
        return withdraw_ledger
   
    print(deposit(amount, description))
    print(withdraw(amount, description))

percentageMap(1000, "kitty")