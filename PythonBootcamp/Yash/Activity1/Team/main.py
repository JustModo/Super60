from check_win import check_win
value = list(range(10))


def main():
    player_x = (input("Enter the name of player X: "))
    player_o = (input("Enter the name of player O: "))

    for i in range(1, 10):
        pattern()
        if (i % 2):
            player = "X"
            profile = player_x
        else:
            player = "O"
            profile = player_o
        place = 100
        while True:
            try:
                place = int(
                    input(f"Enter the position in the above table (0-9): \n{player}: "))
                if 1 <= place <= 9 and str(value[place]).isdigit():
                    value[place] = player
                    break
                elif place < 1 or place > 9:
                    print("Kindly enter a number in the spcified range only")
                elif not str(value[place]).isdigit():
                    print("The entered spot has already been occupied")

            except TypeError:
                print("Kindly enter a number in the specified range")
            except ValueError:
                print("Not Valid")

        if (check_win(place)):
            pattern()
            print(f"Congratulations!, {profile} has won the game")
            return

    pattern()
    print("It's a draw")


def pattern():
    print(f" {value[0+1]}| {value[1+1]} |{value[2+1]} ")
    for i in range(9):
        if i == 2 or i == 6:
            print("+", end="")
        else:
            print("-", end='')
    print()
    print(f" {value[3+1]}| {value[4+1]} |{value[5+1]} ")
    for i in range(9):
        if i == 2 or i == 6:
            print("+", end="")
        else:
            print("-", end='')
    print()
    print(f" {value[6+1]}| {value[7+1]} |{value[8+1]} ")


if __name__ == "__main__":
    main()
