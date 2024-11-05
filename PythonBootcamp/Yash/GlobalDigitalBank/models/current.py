from account import Account


class Current(Account):
    def __init__(self, company_name, registration_number) -> None:
        super().__init__()
        self.company_name = company_name
        self.registration_number = registration_number
        pass
