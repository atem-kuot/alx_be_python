class BankAccount():

    def __init__(self,account_balance ):
        self.account_balance = account_balance 
    
    def deposit (self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.account_balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.account_balance}.")
        elif amount > self.account_balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
    
    def display_balance(self):
        print(f"Current balance: ${self.account_balance}.")
