from models.account import Account
from models.privileges import Privilege


class Savings(Account):
    def __init__(self, date_of_birth: int, gender: str, name: str, balance: int, pin_number: int, privilege: Privilege) -> None:
        super().__init__(name, balance, privilege, pin_number)
        self.date_of_birth = date_of_birth
        self.gender = gender
