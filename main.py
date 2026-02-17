"""
Name: Kevin Paviome
Date: 1/15/2026
Simple OOP Demo - Covers all key concepts in ~50 lines
Week 1 Lab
"""


# CLASS: Blueprint for creating objects
class BankAccount:

    # CONSTRUCTOR: Initializes new objects with __init__()
    # SELF PARAMETER: Refers to the current object instance
    def __init__(self, owner, balance=0):
        # ATTRIBUTES: Store object-specific data
        self.owner = owner
        self.balance = balance

    # METHODS: Define behaviors that objects can perform
    def deposit(self, amount):
        """Add money to account using self to access this object's balance"""
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        # Remove money if sufficient funds exist
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

    def get_info(self):
        # Display account information
        return f"{self.owner}'s account: ${self.balance}"

    # STUDENT EXERCISE METHODS

    def transfer(self, amount, other_account):
        # Transfer money if sufficient funds exist
        if amount > self.balance:
            return "Transfer failed: Insufficient funds!"
        self.balance -= amount
        other_account.balance += amount
        return f"Transferred ${amount} to {other_account.owner}"

    def apply_interest(self, rate):
        self.balance += (self.balance * rate)
        return f"Interest applied. New balance: ${self.balance}"


# DEMONSTRATION

# OBJECTS: Create instances from the class blueprint
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print("Initial Accounts:")
print(account1.get_info())
print(account2.get_info())

print("\nTransactions:")
print(account1.deposit(200))
print(account1.withdraw(300))
print(account2.deposit(1000))

print("\nFinal Balances:")
print(account1.get_info())
print(account2.get_info())

print("\nTesting transfer method:")
print(account1.transfer(100, account2))
print(account1.get_info())
print(account2.get_info())

print("\nTesting apply_interest method:")
print(account1.apply_interest(0.05))  # 5% interest
print(account1.get_info())
