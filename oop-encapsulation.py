class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

# Creating an object of class BankAccount
my_account = BankAccount("123456789", 1000)

# Accessing attributes and methods (Encapsulation protects attributes)
print(my_account.get_balance())  # Output: 1000
my_account.withdraw(500)
print(my_account.get_balance())  # Output: 500
