class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₱{amount}. New balance: ₱{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts money from the balance if sufficient funds are available."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ₱{amount}. New balance: ₱{self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Displays the current balance."""
        print(f"Account balance: ₱{self.balance}")


account = BankAccount(account_number="0917096869", owner="ENCARNACION KRISCHARDALE")


account.deposit(12000)
account.withdraw(3000)  
account.display_balance()
