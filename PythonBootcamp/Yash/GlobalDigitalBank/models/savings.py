from account import Account


class Savings(Account):
    def __init__(self, date_of_birth, phone_number) -> None:
        super().__init__()
        self.date = date_of_birth
        self.phone_number = phone_number
