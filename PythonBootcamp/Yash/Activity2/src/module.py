from unit import Unit
from typing import List


class Module:
    def __init__(self, name: str, *units: Unit) -> None:
        self.__name: str = name
        self.__unit_list: List[Unit] = []
        for unit in units:
            self.__unit_list.append(unit)

    def get_units(self) -> List[Unit]:
        return self.__unit_list

    # Extra

    def get_name(self) -> str:
        return self.__name
