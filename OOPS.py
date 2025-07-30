# Create Account class with 2 attributes - balance and account no. create methods for debit, credit and printing the balance 
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    def get_debit(self, amount):
        self.balance-= amount
        print("Rs.", amount, "debited from your account")
        print("Total balance", self.balance)
    def get_credit(self, amount):
        self.balance+= amount
        print("Rs.", amount, "credited in your account")
        print("Total balance", self.balance)
    def get_balance(self):
        return self.balance
acc_1 = Account(20000, 210203051)
print(acc_1.balance)
print(acc_1.account_no)
acc_1.get_debit(1000)
acc_1.get_credit(500)
