from module import Module
from typing import List


class Course:
    def __init__(self, name: str, *modules: Module) -> None:
        self.__name: str = name
        self.__module_list: List[Module] = []
        for module in modules:
            self.__module_list.append(module)

    def get_modules(self) -> List[Module]:
        return self.__module_list

    # Extra

    def get_name(self) -> str:
        return self.__name
