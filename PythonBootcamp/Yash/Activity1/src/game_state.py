from typing import Tuple, Dict, Final, List

from player_class import Player
from computer_player import Computer

# 0 = X , 1 = O
PLAYER: Final[List[str]] = ['X', 'O']


class GameState:

    def __init__(self, multiplayer: bool, difficulty: int = 0) -> None:
        self.__game: Dict[Tuple[int, int], str] = {}
        self.__game_end = False
        self.__multiplayer = multiplayer
        if (multiplayer):
            self.__players = [
                Player(input("Enter Name: ")), Player(input("Enter Name: "))]
        else:
            self.__players = [
                Player(input("Enter Name: ")), Computer(difficulty)]
        self.__turn = 0

    def update_state(self, position: Tuple[int, int]) -> None:
        try:
            self.__validate_move(position)
        except ValueError:
            raise
        current_player = self.__players[self.__turn]
        if self.__multiplayer:
            self.__game[position] = PLAYER[self.__turn]
            current_player.update_move(position)
        else:
            # Computer Integration
            pass
        self.__evaluate_status()

    def __evaluate_status(self) -> None:
        current_player = self.__players[self.__turn]
        if current_player.has_won():
            self.__game_end = True
            print(f"\n{current_player.name} has Won!")
        elif len(self.__game) == 9:
            self.__game_end = True
            print(f"\nGame is a Draw!")
        else:
            self.__turn = 0 if self.__turn == 1 else 1

    def __validate_move(self, position: Tuple[int, int]) -> None:
        print(len(position))
        if len(position) != 2:
            raise ValueError("\nInvalid Position\n")
        if position in self.__game:
            raise ValueError("\nIllegal Move\n")
        if not all(0 <= value <= 2 for value in position):
            raise ValueError("\nOut of Bounds\n")

    def print_game(self) -> None:
        for i in range(3):
            for j in range(3):
                if (i, j) in self.__game:
                    print(self.__game[(i, j)], end=' ')
                else:
                    print('_', end=' ')
            print()
        print(f"\nIt's {self.__players[self.__turn].name}'s Turn!")

    def is_gameover(self) -> bool:
        return self.__game_end
