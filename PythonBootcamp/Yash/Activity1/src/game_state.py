from typing import Tuple, Dict, Final, List
import time

from player_class import Player
from computer_player import Computer

# 0 = X , 1 = O
PLAYER: Final[List[str]] = ['X', 'O']


class GameState:

    def __init__(self, multiplayer: bool) -> None:
        self.__game: Dict[Tuple[int, int], str] = {}
        self.__game_end = False
        self.__multiplayer = multiplayer
        if (multiplayer):
            self.__players = [
                Player(input("Enter Name: ")), Player(input("Enter Name: "))]
        else:
            self.__players = [
                Player(input("Enter Name: ")), Computer()]
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
            self.__evaluate_status()
        else:
            current_player.update_move(position)
            self.__game[position] = PLAYER[self.__turn]
            self.__evaluate_status()
            # Bot Plays
            if not self.__game_end:
                self.print_game()
                print("Bob is Thinking...")
                time.sleep(2)
                position = self.__players[self.__turn].update_move()
                self.__game[position] = PLAYER[self.__turn]
                self.__evaluate_status()

    def __evaluate_status(self) -> None:
        current_player = self.__players[self.__turn]
        if current_player.has_won():
            self.__game_end = True
            self.print_game()
            print(f"\n{current_player.name} has Won!")
        elif len(self.__game) == 9:
            self.__game_end = True
            self.print_game()
            print(f"\nGame is a Draw!")
        else:
            self.__turn = 0 if self.__turn == 1 else 1
        print()

    def __validate_move(self, position: Tuple[int, int]) -> None:
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
        if not self.__game_end:
            print(f"\nIt's {self.__players[self.__turn].name}'s Turn!\n")

    def is_gameover(self) -> bool:
        return self.__game_end
