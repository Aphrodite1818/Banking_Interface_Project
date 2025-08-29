class Business_Account():
    def __init__(self, account_number :str, account_holder:str, business_name:str, balance : float=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.business_name = business_name
        self.balance = balance

    def withdraw(self, amount:str):
        if amount <=0:
            raise ValueError("Withdrawal of negative amount is not allowed")
        else:
            self.balance -= amount
            return self.balance
        
    def deposit(self, amount:str):
        if amount <=0:
            raise ValueError("Deposit of negative amount is not allowed")
        else:
            self.balance += amount
            return self.balance
        
    def __str__(self):
        return f"Business Account({self.account_number}, {self.account_holder}, {self.business_name}, Balance: {self.balance})"
    
    def __repr__(self):
        return f"Business_Account({self.account_number}, {self.account_holder}, {self.business_name}, {self.balance})"