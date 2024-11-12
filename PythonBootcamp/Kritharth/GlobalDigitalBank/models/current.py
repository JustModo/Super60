from models.account import Account


class Current(Account):
    def __init__(self, name: str, balance: float, pin_number: int, is_active: bool, privilege: str,website_url:str,registration_number:int) -> None:
        super().__init__(name, balance, pin_number, is_active, privilege)
        self.website_url = website_url
        self.registration_number = registration_number