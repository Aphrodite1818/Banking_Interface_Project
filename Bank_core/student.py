class Student_Account():
    def __init__(self, account_number: str, account_holder :str, school_name :str, balance : float =0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.school_name = school_name
        self.balance = balance

    def withdraw(self, amount:str):
        if amount <=0:
            raise ValueError("Withdrawal of negative amount is not allowed")
        


        elif amount >50000:
            raise ValueError("You cannot withdraw more than 50000 at a time")
        

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
        
    
    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Student Account({self.account_number}, {self.account_holder}, {self.school_name}, Balance: {self.balance})"
    


    def __repr__(self):
        return f"Student_Account({self.account_number}, {self.account_holder}, {self.school_name}, {self.balance})"