from models.account import Account


class Savings(Account):
    def __init__(self, name: str,gender:str, balance: float, pin_number: int, is_active: bool, privilege: str,date_of_birth:str) -> None:
        super().__init__(name, balance, pin_number, is_active, privilege)
        self.date_of_birth = date_of_birth
        self.gender = gender