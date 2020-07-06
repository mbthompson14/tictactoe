def print_table(table):
    print("-" * 9)
    print("| " + table[0][0] + " " + table[0][1] + " " + table[0][2] + " |")
    print("| " + table[1][0] + " " + table[1][1] + " " + table[1][2] + " |")
    print("| " + table[2][0] + " " + table[2][1] + " " + table[2][2] + " |")
    print("-" * 9)


def input_is_num():
    c = input("Enter coordinates: ").split()
    while not c[0].isnumeric() or not c[1].isnumeric():
        print("You should enter numbers!")
        c = input("Enter coordinates: ").split()
    return c


def in_range(c):
    c = [int(c[0]), int(c[1])]
    while not(1 <= c[0] <= 3) or not(1 <= c[1] <= 3):
        print("Coordinates should be from 1 to 3!")
        c = input_is_num()
        c = [int(c[0]), int(c[1])]
    return c


def convert_coord(c):
    c = [c[1] - 1, c[0] - 1]
    if c[0] == 0:
        c = [2, c[1]]
    elif c[0] == 2:
        c = [0, c[1]]
    return c


x = "         "
cells = [[x for x in x[0:3]],
         [x for x in x[3:6]],
         [x for x in x[6:9]]]  # build matrix

print_table(cells)


# CHECK TABLE STATE:
def check_table_state(cells):
    cells_t = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    for i in range(len(cells_t)):
        for j in range(len(cells_t[0])):
           cells_t[i][j] = cells[j][i]  # transpose matrix

    # determine if 3 x's in a row - if yes, x win
    if cells[0].count('X') == 3 or cells[1].count('X') == 3 or cells[2].count('X') == 3 \
            or cells_t[0].count('X') == 3 or cells_t[1].count('X') == 3 or cells_t[2].count('X') == 3 \
            or cells[0][0] == cells[1][1] == cells[2][2] == 'X' \
            or cells[0][2] == cells[1][1] == cells[2][0] == 'X':
        x_win = True
    else:
        x_win = False

    # determine if 3 o's in a row - if yes, o win
    if cells[0].count('O') == 3 or cells[1].count('O') == 3 or cells[2].count('O') == 3 \
            or cells_t[0].count('O') == 3 or cells_t[1].count('O') == 3 or cells_t[2].count('O') == 3 \
            or cells[0][0] == cells[1][1] == cells[2][2] == 'O' \
            or cells[0][2] == cells[1][1] == cells[2][0] == 'O':
        o_win = True
    else:
        o_win = False

    # determine if all cells are filled
    if x_win is False and o_win is False:
        check = [n == " " for n in cells for n in n]
        if any(check):
            finished = False
        else:
            finished = True

    impossible = False
    if (cells[0].count('X') + cells[1].count('X') + cells[2].count('X')) >= 2 + (cells[0].count('O') + cells[1].count('O') + cells[2].count('O')) \
            or (cells[0].count('O') + cells[1].count('O') + cells[2].count('O')) >= 2 + (cells[0].count('X') + cells[1].count('X') + cells[2].count('X')):
        impossible = True

    if x_win and o_win or impossible:
        return 4
        # print("Impossible")
    elif x_win:
        return 2
        # print("X wins")
    elif o_win:
        return 3
        # print("O wins")
    elif not finished:
        return 0
        # print("Game not finished")
    elif finished and x_win is False and o_win is False:
        return 1
        # print("Draw")
    else:
        return 4
        # print("Impossible")


# MAKE A MOVE:
counter = 0
while True:
    coord = input_is_num()
    coord = in_range(coord)
    coord = convert_coord(coord)

    while cells[coord[0]][coord[1]] == 'X' or cells[coord[0]][coord[1]] == 'O':
        print("This cell is occupied! Choose another one!")
        coord = input_is_num()
        coord = in_range(coord)
        coord = convert_coord(coord)

    if counter % 2:
        cells[coord[0]][coord[1]] = 'O'
    elif not(counter % 2):
        cells[coord[0]][coord[1]] = 'X'

    counter += 1

    print_table(cells)

    table_state = check_table_state(cells)

    if table_state == 1:
        print("Draw")
        break
    elif table_state == 2:
        print("X wins")
        break
    elif table_state == 3:
        print("O wins")
        break
    elif table_state == 4:
        print("Impossible")
        break


