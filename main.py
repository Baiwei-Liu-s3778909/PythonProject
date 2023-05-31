from bank import Bank
from manage_bank import Manage_bank

manage_bank = Manage_bank("this is Bank System")

account1 = Bank(1, 10000.00)
account2 = Bank(2, 15000.00)
account3 = Bank(3)

manage_bank.add_account(account1)
manage_bank.add_account(account2)
manage_bank.add_account(account3)

manage_bank.display_account()


account1.deposit(1000.00)
account2.withdraw(1000.00)
account3.withdraw(1000.00)
manage_bank.display_account()




