from repositories.account_repository import AccountRepository


class Account:
    def __init__(self, name:str, balance:int, privilege:str, pin_number:int) -> None:
        self.account_number:int = AccountRepository.generate_account_number()
        self.name = name
        self.pinNumber = pin_number
        self.balance = balance
        self.privilege = privilege
        self.isActive = True
        self.close_date = None
