from player_class import Player
from typing import List, Tuple
import random


class Computer(Player):

    def __init__(self) -> None:
        super().__init__(name='Bob')

    def update_move(self) -> Tuple[int, int]:
        number_of_moves = len(self.moves)
        random_index = random.randint(0, number_of_moves-1)
        position = self.moves[random_index]
        super().update_move(position)
        print(self.moves)
        return position
