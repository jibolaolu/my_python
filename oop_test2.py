#Create an Account that accepts deposit and withdrawal

class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,depos_amt):
        self.balance = self.balance + depos_amt
        print("We have added {} to your account balance".format(depos_amt))

    def withdrawal(self, withdr_amt):
        if self.balance >= withdr_amt:
            self.balance = self.balance - withdr_amt
            print("You are withdrawing {} and your new balance is {}".format(withdr_amt, self.balance))
        else:
            print("Sorry you don't have enough balance to make your withdrawal")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"


ac=Account('Sam', 500)
print("This is {}'s account with the balance of {}".format(ac.owner, ac.balance))

ac.deposit(300)
print("Your new balance is {}".format(ac.balance))

ac.withdrawal(800)
print("Your new balance is {}".format(ac.balance))


