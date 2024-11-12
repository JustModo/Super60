from models.privileges import Privilege
from typing import Dict


class AccountPrivilegeList:
    privileges: Dict[Privilege, int] = {
        'PREMIUM': 100000,
        'GOLD': 50000,
        'SILVLER': 25000,
    }

    @classmethod
    def get_transfer_limit(cls, privilege: str) -> int:
        return cls.privileges.get(privilege, 0)
