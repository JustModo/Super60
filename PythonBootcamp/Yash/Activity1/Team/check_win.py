
mapping = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

row = [[0, 0, 0], [0, 0, 0]]
col = [[0, 0, 0], [0, 0, 0]]
diag = [[0, 0], [0, 0]]

turn = 0


def check_win(place: int):
    position = mapping[place]
    x = position[0]
    y = position[1]
    global turn

    row[turn][x] += 1
    col[turn][y] += 1
    if x == y:
        diag[turn][0] += 1
    if x + y == 2:
        diag[turn][1] += 1

    _turn = turn

    turn = 1 if turn == 0 else 0

    return any(3 in lst for lst in [row[_turn], col[_turn], diag[_turn]])
