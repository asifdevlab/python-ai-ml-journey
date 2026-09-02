# Q1. Create a class BankAccount with:
#    Attributes: account_number, owner_name, balance
#    Methods: deposit, withdraw, check_balance

class BankAccount:

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print(f"{deposit_amount} rupees is succesfully deposited")

    def withdraw(self, withdraw_amount):
        if(self.balance >= withdraw_amount):
            self.balance -= withdraw_amount
            print(f"{withdraw_amount} rupees withdrawl success")
        else:
            print("Cannot withdraw, Insufficient Balance!")

    def check_balance(self):
        print(f"Balance = {self.balance}")

acc1 = BankAccount(101,"Asif Hussain",800)
acc1.check_balance()
acc1.deposit(200)
acc1.check_balance()
acc1.withdraw(500)
# acc1.withdraw(1100) prints "Cannot withdraw, Insufficient Balance!"
acc1.check_balance()




        