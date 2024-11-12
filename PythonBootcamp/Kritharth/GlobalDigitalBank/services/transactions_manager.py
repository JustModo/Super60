import datetime

class TransactionManager:
    transaction_log = []

    @classmethod
    def log_transaction(cls,account_number:int,amount:int,transaction_type:str,to_account_number:int):
        transaction_record = {
            'account_number' : account_number,
            'amount' : amount,
            'transaction_type' : transaction_type,
            'date' : cls.get_current_timestamp(),
            'to_account_number' : to_account_number
        }
        cls.transaction_log.append(transaction_record)