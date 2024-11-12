from exceptions.exceptions import AccountNotActiveException, InsufficientFundsException, InvalidPinException, TransferLimitExceededException
from models.account import Account
from models.savings import Savings
from models.current import Current
from repositories.account_repository import AccountRepository
from services.account_privileges_manager import AccountPrivilegeList
from services.transaction_manager import TransactionManager
# Open Accounts /
# Close Accounts
# Withdrawl /
# deposit /
# Transfer
# Check if Acccount is active /
# Validate pin number /


class AccountManager:
    def open_account(self, account_type, **kwargs) -> Account:
        if account_type == 'savings':
            new_account = Savings(**kwargs)
        elif account_type == "current":
            new_account = Current(**kwargs)
        else:
            raise ValueError("Not Valid Account Type")

        AccountRepository.save_aacount(new_account)
        return new_account

    def check_account_active(self, account: Account) -> None:
        if not account.is_active:
            raise AccountNotActiveException('Account is not Active')

    def validate_pin(self, account: Account, pin_number) -> None:
        if account.pin_number != pin_number:
            raise InvalidPinException("Invalid Pin")

    def withdraw(self, account: Account, amount: int, pin_number: int) -> None:
        self.check_account_active(account)
        self.validate_pin(account, pin_number)

        if account.balance < amount:
            raise InsufficientFundsException("Insufficient funds")

        account.balance -= amount
        TransactionManager.log_transaction(
            account.account_number, amount, 'withdraw')

    def deposit(self, account: Account, amount: int,) -> None:
        self.check_account_active(account)

        account.balance += amount
        TransactionManager.log_transaction(
            account.account_number, amount, "deposit")

    def transfer(self, from_account: Account, to_account: Account, amount: int, pin_number: int) -> None:
        self.check_account_active(from_account)
        self.check_account_active(to_account)
        self.validate_pin(from_account, pin_number)

        if from_account.balance < amount:
            raise InsufficientFundsException('Insufficient Funds')

        limit = AccountPrivilegeList.get_transfer_limit(from_account.privilege)
        if amount > limit:
            raise TransferLimitExceededException("Transfer Limit Exceeded")

        from_account.balance -= amount
        to_account.balance += amount
        TransactionManager.log_transaction(
            from_account.account_number, amount, 'transfer', to_account.account_number)

    def close_account(self, account: Account) -> None:
        if not account.is_active:
            raise AccountNotActiveException("Account Deactivated Already")

        account.is_active = False
