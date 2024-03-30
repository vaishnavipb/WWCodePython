# Day 60: Create a class representing a simple bank account with deposit and withdraw methods

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        print(f"Deposited the amount: {amount}")
        print(f"The new balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds, cannot withdraw")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"New balance: {self.balance}")

    def current_balance(self):
        print(f"Current balance is: {self.balance}")


account = BankAccount(100)
account.deposit(100000)
account.withdraw(10)
account.current_balance()
