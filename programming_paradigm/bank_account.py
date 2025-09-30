class BankAccount():
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.accountBalance += amount
            return True
        
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.accountBalance:
            self.accountBalance -= amount
            return True    
        return False
        
    def display_balance(self):
        print(f"Current balance: ${self.accountBalance: 2f}")