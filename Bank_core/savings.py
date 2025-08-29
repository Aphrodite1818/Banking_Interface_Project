class Savings_Account():
    def __init__(self, account_number:str, account_holder:str, interest_rate:float, balance :str=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.interest_rate = interest_rate
        self.balance = balance

    def withdraw(self, amount:str):
        if amount <=0:
            raise ValueError("Withdrawal of negative amount is not allowed")
        
        elif amount > 100000:
            raise ValueError("You cannot withdraw more than 100000 at a time")
        
        elif amount > self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount
            return self.balance
        
    def deposit(self, amount:str):
        if amount <=0:
            raise ValueError("Deposit of negative amount is not allowed")
        else:
            self.balance += amount
            return self.balance
        
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        return self.balance
    
    def check_balance(self):
        if self.balance < 1000:
            raise ValueError("Minimum balance of 1000 is required")
        else:
            return self.balance
        
    def __str__(self):
        return f"Savings Account({self.account_number}, {self.account_holder}, {self.interest_rate}%, Balance: {self.balance})"
    
    def __repr__(self):
        return f"Savings_Account({self.account_number}, {self.account_holder}, {self.interest_rate}%, {self.balance})"