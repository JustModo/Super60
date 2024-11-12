# Open Accounts
# Close Accounts
# Withdrawl
# Transfer
#Check if account is active
# Validate pin number



from transactions_manager import TransactionManager
from models.account import Account
from models.savings import Savings
from models.current import Current
from repositories.account_repository import AccountRepository
from exceptions.exceptions import *
from services.transactions_manager import TransactionManager
from services.account_privileges_manager import AccountPrivilegesManager


class AccountManager:
    def open_account(self,account_type,**kwargs):
        if account_type == 'savings':
            new_account = Savings(**kwargs)
        elif account_type == 'current':
            new_account = Current(**kwargs)
        else:
            raise ValueError('Invalid account type')
    
        AccountRepository.save_account(new_account):
        return new_account
    
    def check_account_action(self,account:Account):
        if not account.is_active:
            raise InvalidPinException('Invalid Pin')
        
    def withdraw(self,account:Account,amount:int,pin_number):
        self.check_account_active(account)
        self.validate_pin(account,pin_number)

        if account.balance < amount:
            raise InsufficientFundsException('Insufficient Funds')
        
        account.balance -= amount
        TransactionManager.log_transaction(account.account_number,amount,'withdraw')

    def deposit(self,account:Account,amount:int):
        self.check_account_active(account)

        account.balance += amount
        TransactionManager.log_transaction(account.account_number,amount,'deposit')

    def transfer(self,from_account:Account,to_account:Account,amount:int,pin_number:int)->None:
        self.check_account_active(from_account)
        self.check_account_active(to_account)
        self.validate_pin(from_account,pin_number)

        if from_account.balance < amount:
            raise InsufficientFundsException('Insufficient Funds')
        
        limit = AccountPrivilegesManager.get_transfer_limit(from_account.privilege)
        if amount > limit:
            raise TransferLimitExceedException('Transfer limit Exceeded')
        
        from_account.balance -= amount
        to_account.balance += amount
        TransactionManager.log_transaction(from_account.account_number,amount,'transfer',to_account.account_number)

    def close_account(self,account:Account):
        if not account.is_active:
            raise AccountNotActiveException('Account Deactivated Alreaady')
        
    

