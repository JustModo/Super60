

from typing import List

from models.account import Account


class AccountRepository:
    accounts: List[Account] = []
    account_counter = 1000

    # Method to  generate a new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter

    # Method to save accounts
    @classmethod
    def save_aacount(cls, accounts):
        cls.accounts.append(accounts)

    # Method to get all accounts
    @classmethod
    def get_all_accounts(cls):
        return cls.accounts
