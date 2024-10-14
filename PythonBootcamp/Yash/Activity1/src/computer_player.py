from player_class import Player
from typing import List, Tuple
import random


class Computer(Player):
    def __init__(self, difficulty: int) -> None:
        super().__init__(name='Bob')
        self.__difficulty = difficulty
        self.__moves: List = [(i, j) for i in range(3) for j in range(3)]

    def __update_move(self, positon: Tuple[int, int]) -> None:
        super().update_move(positon)
        if positon in self.__moves:
            self.__moves.remove(positon)

    def evaluate_move(self) -> None:
        number_of_moves = len(self.__moves)
        random_index = random.randint(0, number_of_moves-1)
        self.__update_move(self.__moves.pop(random_index))
