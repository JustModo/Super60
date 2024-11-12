from repositories.account_repository import AccountRepository
from models.privileges import Privilege


class Account:
    def __init__(self, name: str, balance: int, privilege: Privilege, pin_number: int) -> None:
        self.account_number = AccountRepository.generate_account_number()
        self.name = name
        self.balance = balance
        self.privilege = privilege
        self.pin_number = pin_number
        self.is_active = True
        self.closed_date = None
