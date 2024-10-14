from game_state import GameState


def main():
    while True:
        print("\nTic Tac Toe\n")
        multi = True
        game = GameState(multi, 0)
        print("\nAll the Best!\n")
        while not game.is_gameover():
            game.print_game()
            print()
            try:
                postion = tuple(map(int, input("Enter position: ").split()))
                game.update_state(postion)
                print()
            except ValueError as e:
                print(e)
        print("Wanna Play Again? [Y]es / [N]o")
        res = input().lower()
        if not (res == 'y' or res == 'yes'):
            break


if __name__ == "__main__":
    main()
