class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("\nDeposit amount must be positive.\n")
        return self.balance

    def withdraw(self, spent):
        if self.balance >= spent:
            self.balance -= spent
            print(f"Spent ${spent}. New balance: ${self.balance}")
        else:
            print("\nInsufficient funds in the account\n")
        return self.balance

bankAccount = BankAccount(0)
bankAccount.deposit(0)
bankAccount.deposit(100)
bankAccount.withdraw(75)
bankAccount.withdraw(250)