from bank import Bank

class Manage_bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, bank):
        self.accounts.append(bank)
        print("Add ", bank.get_account_number(), " succussfully")
        print("--------------------------------------------------")

    def remove_account(self, bank):
       self.accounts.remove(bank)

    def display_account(self):
        print("This is all account in bank:")
        for bank in self.accounts:
            print("Account Number:", bank.get_account_number())
            print("Balance:", bank.get_balance())
            print("")