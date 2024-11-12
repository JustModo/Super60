class AccountRepository:
    # class attribute to store all the elements
    accounts = []
    account_counter = 1000

    #Method to generate new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter
    
    # class method takes cls as its first argument
    # instance/regular method takes self as its first argument
    # static method takes neither self nor cls as its first argument

    #Method to save account
    @classmethod
    def save_account(cls,account):
        cls.account.append(account)

    #Method to get all accounts
    def get_all_accounts(self):
        return self.account
