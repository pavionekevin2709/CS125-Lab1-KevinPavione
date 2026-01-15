"""
Name: Zach Wilson
Date: 1/15/2026
Course: CS 125
Simple OOP Demo - Covers all key concepts in ~50 lines
"""


# CLASS: Blueprint for creating objects
class BankAccount:

    # CONSTRUCTOR: Initializes new objects with __init__()
    # SELF PARAMETER: Refers to the current object instance
    def __init__(self, owner, balance=0):
        # ATTRIBUTES: Store object-specific data
        self.owner = owner  # Each account has its own owner
        self.balance = balance  # Each account has its own balance

    # METHODS: Define behaviors that objects can perform
    def deposit(self, amount):
        """Add money to account using self to access this object's balance"""
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        # Remove money if sufficient funds exist
        if amount > self.balance:
            return # Insufficient funds!
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

    def get_info(self):
        # Display account information
        return f"{self.owner}'s account: ${self.balance}"

    # STUDENT EXERCISE
    # TODO: Create two new methods below:
    # 1. transfer(self, amount, other_account) - transfers money to another account
    # 2. apply_interest(self, rate) - adds interest to the balance
    #


# DEMONSTRATION

# OBJECTS: Create instances from the class blueprint
account1 = BankAccount("Alice", 1000)  # Object with $1000
account2 = BankAccount("Bob", 500)  # Different object with $500

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

# Each object maintains its own state independently!

# DEMO YOUR NEW METHODS HERE
# Once you've created your two methods above, test them here!
# Example calls (uncomment after implementing):
#
# print("\nTesting transfer method:")
# print(account1.transfer(100, account2))
# print(account1.get_info())
# print(account2.get_info())
#
# print("\nTesting apply_interest method:")
# print(account1.apply_interest(0.05))  # 5% interest
# print(account1.get_info())
#