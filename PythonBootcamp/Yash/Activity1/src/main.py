from game_state import GameState


def main():
    while True:
        print("\nTic Tac Toe\n")
        res = input("Do you have Friends? ").lower()
        multiplayer: bool
        if (res == 'y' or res == 'yes'):
            multiplayer = True
        else:
            multiplayer = False
        game = GameState(multiplayer)
        print("\nAll the Best!\n")
        while not game.is_gameover():
            game.print_game()
            try:
                position = tuple(map(int, input("Enter position: ").split()))
                game.update_state(position)
            except ValueError as e:
                print(e)
        print("Wanna Play Again? [Y]es / [N]o")
        res = input().lower()
        if not (res == 'y' or res == 'yes'):
            break


if __name__ == "__main__":
    main()
