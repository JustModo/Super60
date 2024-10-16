from player_class import Player
from typing import List, Tuple
import random


class Computer(Player):

    def __init__(self) -> None:
        super().__init__(name='Bob')

    def update_move(self, moves) -> Tuple[int, int]:
        number_of_moves = len(moves)
        random_index = random.randint(0, number_of_moves-1)
        position = moves[random_index]
        super().update_move(position)
        # print(moves)
        return position
