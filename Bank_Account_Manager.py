# Bank Account Manager
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print("Name:", self.name)
        print("Balance:", self.balance)
        print()


accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

account_objects = []

for name, acc_no, balance in accounts:
    account_objects.append(BankAccount(name, acc_no, balance))

for account in account_objects:
    if account.account_number == "A002":
        account.deposit(3000)

    elif account.account_number == "A003":
        account.withdraw(15000)

    elif account.account_number == "A001":
        account.withdraw(2000)

print("\nFinal Balances:")
for account in account_objects:
    account.get_balance()