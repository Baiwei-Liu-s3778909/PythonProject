class Bank:


    def __init__(self, account_number, balance = 0.0):
        self.account_number = int(account_number)
        self.balance = float(balance)
    
    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit account number ", self.account_number, " succussfully")
        print("--------------------------------------------------")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw account number ", self.account_number, " succussfully")
            print("--------------------------------------------------")
        else: 
            print("Account number ",self.account_number,"'s balance is insufficient !")
            print("--------------------------------------------------")
        