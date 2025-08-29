class Current_Account():
    def __init__(self, account_number : str, account_holder :str, balance : float =0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount:float):
        if amount < 0:
            raise ValueError("Withdrawal of negative amount is not allowed")
        elif amount > self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= (amount/0.3) +(amount)
            return self.balance
        
    def deposit(self, amount:float):
        if amount < 0:
            raise ValueError("Deposit of negative amount is not allowed")
        else:
            self.balance += amount
            return self.balance
        
    def check_balance(self):
        return self.balance
    

    def __str__(self):
        return f"Current Account({self.account_number}, {self.account_holder}, Balance: {self.balance})"
    
    def __repr__(self):
        return f"Current_Account({self.account_number}, {self.account_holder}, {self.balance})"
    
