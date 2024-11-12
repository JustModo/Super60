from models.savings import Savings
from models.current import Current
from services.account_privileges_manager import AccountPrivilegesManager
from services.account_manager import AccountManager
from services.transactions_manager import TransactionManager
from exceptions.exceptions import *
from repositories.account_repository import AccountRepository

class AccountUI:
    def start(self):
        while True:
            print('''Welcome to Global Digital Bank
                Select an option
                1.Open Account
                2.Close Account
                3.Withdrawl Funds
                4.Deposit Funds
                5.Trsnsfer Funds
                9.Exit
                ''')
            
            choice = int(input('Enter your choice:'))

            match choice:
                case 1:
                    self.open_account()
                case 2:
                    self.close_account()
                case 3:
                    self.withdraw_funds()
                case 4:
                    self.deposit_funds()
                case 5:
                    self.transfer_funds()
                case 9:
                    break
                case _:
                    print('Invalid choice!Please try again')

    
    def open_account(self):
        account_type = input('Enter account typr(savings/current): ').strip().lower()
        name = input('Enter your name: ')
        amount = float(input('Enter initial deposit amount:'))
        pin_number = int(input('Enter your pin number: '))
        privilege = input('Enter the account privilege(Premium/Gold/Silver)').strip().lower()

        if account_type == 'savings':
            date_of_birth = input('Enter your date of birth(yyyy-MM-DD): ')
            gender = input('Enter your gender(M/F): ')
            account = AccountManager().open_account(account_type, name = name, balance = amount, date_of_birth = date_of_birth, gender = gender, pin_number = pin_number, privilege = privilege)

        elif account_type == 'current':
            registration_number = input('Enter your registration number: ')
            website_url = input('Enter your website URL: ')
            account = AccountManager().open_account(account_type, name = name, balance = amount, registration_number = registration_number, website_url = website_url, pin_number = pin_number,privilege = privilege)
        else:
            print('Invalid account type. Please try again')
            return

        print(account_type.capitalize(),'Account Opened Successfully! Account Number: ',account.account_number)


    def close_account(self):
        account_number = int(input('Enter your account number: '))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number))

        if account:
            try:
                AccountManager().close_account(account)
                print('Account closed successfully')
            except Exception as e:
                print("Error: ",e)
        else:
            print('Account Not Found. Please try again')

    def withdraw_funds(self):
        account_number = int(input('Enter your account number: '))
        amount = (float(input('Enter the amount to withdraw: ')))
        pin_number = int(input('Enter your pin number: '))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number),None)
        
        if account:
            try:
                AccountManager.withdraw(account, amount, pin_number)
                print('Amount withdrawn successfully!')
            except Exception as e:
                print("Error: ",e)
        else:
            print('Account Not Found. Please Try Again')



    def deposit_funds(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter amount to deposit: "))
        account = next(
            (acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().deposit(account, amount)
                print("Amount deposited successfully")
            except Exception as e:
                print("Error:", e)
        else:
            print("Account not found. Please try again.")


    def transfer_funds(self):
        to_account_number = int(input('To account number: '))
        from_account_number = int(input('From account number: '))
        amount = float(input('Enter amount to be transferred: '))
        account_to = next(acc for acc in AccountRepository.accounts if acc.account_number == to_account_number)
        account_from = next(acc for acc in AccountRepository.accounts if acc.account_number == from_account_number)
        
        if account_from and account_to:
            try:
                pin_number = int(input('Enter your pin number: '))
                AccountManager().transfer(account_from,account_to,amount,pin_number)
                print('Amount transferred successfully!')
            except Exception as e:
                print("Error: ",e)
        else:
            print("Account Not Found! Please try again")
            return
        

    