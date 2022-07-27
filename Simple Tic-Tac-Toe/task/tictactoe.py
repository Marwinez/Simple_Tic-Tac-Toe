def board_print():
    print("---------")
    for i in range(3):
        print("|", board[i][0], board[i][1], board[i][2], "|")
    print("---------")


def win():
    for i in range(0, 2):
        if board[0][i] == board[1][i] == board[2][i] == current:
            return True
        if board[i][0] == board[i][1] == board[i][2] == current:
            return True
    if board[0][0] == board[1][1] == board[2][2] == current:
        return True
    elif board[2][0] == board[1][1] == board[0][2] == current:
        return True


board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board_print()

current = "X"
player = 1
game = True
move_counter = 0
while move_counter < 9:
    coords = str(input()).split(" ")
    try:
        coords = [int(coord) for coord in coords]
    except ValueError:
        print("You should enter numbers!")
    else:
        try:
            coord_1 = int(coords[0]) - 1
            coord_2 = int(coords[1]) - 1
        except IndexError:
            print("You should enter two numbers!")
        try:
            if board[coord_1][coord_2] == " " or board[coord_1][coord_2] == "_":
                board[coord_1][coord_2] = current
                board_print()
                move_counter += 1
                if win():
                    print(current, "wins")
                    break
                else:
                    if player == 1:
                        player = 2
                        current = "O"
                    else:
                        player = 1
                        current = "X"
            else:
                print("This cell is occupied! Choose another one!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")
else:
    print("Draw")



