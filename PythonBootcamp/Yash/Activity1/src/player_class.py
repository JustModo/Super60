from typing import List, Tuple


class Player:

    # moves: List[Tuple[int, int]] = [
    #     (i, j) for i in range(3) for j in range(3)]

    def __init__(self, name: str) -> None:
        self.name = name
        self.__row: List[int] = [0, 0, 0]
        self.__column: List[int] = [0, 0, 0]
        self.__diag: List[int] = [0, 0]

    def update_move(self, position: Tuple[int, int]) -> None:
        x = position[0]
        y = position[1]
        self.__row[x] += 1
        self.__column[y] += 1
        if x == y:
            self.__diag[0] += 1
        if x + y == 2:
            self.__diag[1] += 1
        # if position in self.moves:
        #     self.moves.remove(position)

    def has_won(self) -> bool:
        return any(3 in lst for lst in [self.__row, self.__column, self.__diag])
