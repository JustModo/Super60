from repositories.account_repository import AccountRepository
from services.account_manager import AccountManager


class AccountUI:

    def start(self) -> None:
        while True:
            print('\nWe1come to Global Digital Bank')
            print('\nSelect an option')
            print('1. Open Account')
            print('2. Close Account')
            print('3. Withdraw Funds')
            print('4. Deposit Funds')
            print('5. Transfer Funds')
            print('9. Exit')

            choice = int(input())

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
                case 6:
                    break
                case _:
                    print("Not Valid")

    def open_account(self) -> None:
        account_type = input(
            "Enter account type (savings/current): ").strip().lower()
        name = input("Enter account holder's name: ")
        amount = int(input("Enter initial balance: "))
        pin_number = int(input("Set a 4-digit PIN: "))
        privilege = input(
            "Enter account privilege type: (PREMIUM/GOLD/SILVER)").strip().upper()

        if account_type == 'savings':
            date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
            gender = input("Enter your gender (M/F): ")

            account = AccountManager().open_account(
                account_type=account_type,
                name=name,
                balance=amount,
                date_of_birth=date_of_birth,
                gender=gender,
                pin_number=pin_number
            )

        elif account_type == 'current':
            registration_number = input("Enter your registration number: ")
            website_url = input("Enter your website URL: ")

            account = AccountManager().open_account(
                account_type=account_type,
                name=name,
                balance=amount,
                registration_number=registration_number,
                website_url=website_url,
                pin_number=pin_number,
                privilege=privilege
            )

        else:
            print("Invalid account type. Please try again.")
            return

        print(account_type.capitalize(
        ), "Account opened successfully. Account Number: ", account.account_number)

    def close_account(self) -> None:
        account_number = int(input("Enter your account number: "))
        account = next(
            (acc for acc in AccountRepository.accounts if acc.account_number == account_number))

        if account:
            try:
                AccountManager().close_account(account)
                print('Account closed successfully')
            except Exception as e:
                print("Error: ", e)

        else:
            print('Account Not Found. Please try again')

    def withdraw_funds(self) -> None:
        account_number = input("Enter your account number: ")
        amount = float(input("Enter amount to withdraw: "))
        pin_number = int(input("Enter your pin number: "))

        account = next(
            (acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().withdraw(account, amount, pin_number)
                print("Amount withdrawn successfully")
            except Exception as e:
                print("Error:", e)
        else:
            print("Account not found. Please try again.")

    def deposit_funds(self) -> None:
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


    def transfer_funds(self) -> None:
        from_account_number = int(input("Enter your account number: "))
        to_account_number = int(
            input("Enter your recipient's number: "))
        amount = float(input("Enter amount to deposit: "))
        pin_number = int(input("Enter your pin number: "))

        from_account = next(
            (acc for acc in AccountRepository.accounts if acc.account_number == from_account_number), None)
        to_account = next(
            (acc for acc in AccountRepository.accounts if acc.account_number == to_account_number), None)

        if from_account and to_account:
            try:
                AccountManager().transfer(from_account, to_account, amount, pin_number)
                print("Amount deposited successfully")
            except Exception as e:
                print("Error:", e)
        else:
            print("Accounts not found. Please try again.")
