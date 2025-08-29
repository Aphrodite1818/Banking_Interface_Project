class Current_Account():
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal of negative amount is not allowed")
        elif amount > self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount
            return self.balance
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit of negative amount is not allowed")
        else:
            self.balance += amount
            return self.balance