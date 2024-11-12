from repositories.account_repository import AccountRepository 

class Account:
    def __init__(self,name:str,balance:float,pin_number:int,is_active:bool,privilege:str) -> None:
        self.account_number = AccountRepository.generate_account_number()
        self.name = name
        self.balance = balance
        self.pin_number = pin_number
        self.is_active = is_active
        self.privilege = privilege
        self.is_active = True
        self.closed_date = None