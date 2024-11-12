import datetime
from typing import Optional


class TransactionManager:
    transaction_log: list = []

    @staticmethod
    def get_current_timestamp():
        return datetime.datetime.now()

    @classmethod
    def log_transaction(
        cls,
        account_number: int,
        amount: float,
        transaction_type: str,
        to_account_number: Optional[str] = None
    ) -> None:
        transaction_record = {
            'account_number': account_number,
            'amount': amount,
            'transaction_type': transaction_type,
            'date': cls.get_current_timestamp(),
            'to_account_number': to_account_number
        }
        cls.transaction_log.append(transaction_record)
