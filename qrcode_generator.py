class withdraw_exceptions(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amount, account_no):
        self.balance=initial_amount
        self.name=account_no
        print(
            f"\nAccount {self.name} created. \n Balance = Rs.{self.balance:.2f}"
        )
    def get_balance(self):
        print(f"\nBalance = {self.balance:.2f}...")
    
    def deposit(self,amount=float):
        self.balance =self.balance +  amount
        print(f"\n The amount {amount:.2f} has been added in the account of {self.name} \n New Balance = {self.balance:.2f}")
    def viable_Transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise withdraw_exceptions(f"\n Sorry the account{self.name} does not have enough amount to make the transaction....")
    
    def withdraw(self,amount):
        try:
            self.viable_Transaction(amount)
            self.balance-=amount
            print("\nWithdraw Completed/...")
            self.get_balance()
        except withdraw_exceptions as error:
            print(f"Looks like theres an error {error}")
            self.get_balance()

      

    def transfer(self, amount, name):
        try:
            print("\n  /////////////   Transefer    /////////////")
            self.viable_Transaction(amount)
            self.withdraw(amount)
            name.deposit(amount)
            print("\n///////////////    Transfer completed    /////////////////")
        except withdraw_exceptions as error:
            print("//////////// Transfer denied ///////////////")

class interest_stuff(BankAccount):
    def deposit(self,amount):
        self.balance += (amount*1.09)
        print("Deposit completed....")
        self.get_balance()

class savings (interest_stuff):
    def __init__(self, initial_amount, account_no):
        super().__init__(initial_amount, account_no)
        self.fee=8

    def withdraw(self, amount):
        try :
            self.viable_Transaction(amount*self.fee)
            self.balance-=(amount+self.fee)
            print("Withdraw completed... ")
            self.get_balance()
        except BaseException as error:
            print(f"Withdraw interrupted {error}....")