class BankAccount():
    def __init__(self, account_balance = 0):
        self.accountBalance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.accountBalance += amount
            return True
        
        return False
    
    def withdraw(self, amount):
        if amount < self.accountBalance or amount > 0:
            self.accountBalance -= amount
            return True
        
        return False
    
    def display_balance(self):
        print(f"Current balance: ${self.accountBalance}")