from typing import List, Tuple


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__row: List[int] = [0, 0, 0]
        self.__column: List[int] = [0, 0, 0]
        self.__diag: List[int] = [0, 0]

    def update_move(self, positon: Tuple[int, int]) -> None:
        x = positon[0]
        y = positon[1]
        self.__row[x] += 1
        self.__column[y] += 1
        if x == y:
            self.__diag[0] += 1
        if x + y == 2:
            self.__diag[1] += 1

    def has_won(self) -> bool:
        return any(3 in lst for lst in [self.__row, self.__column, self.__diag])