from models.account import Account
from models.privileges import Privilege


class Current(Account):
    def __init__(self,  registration_number: int, website_url: str, name: str, balance: int, pin_number: int, privilege: Privilege) -> None:
        super().__init__(name, balance, pin_number, privilege)
        self.registration_number = registration_number
        self.website_url = website_url
