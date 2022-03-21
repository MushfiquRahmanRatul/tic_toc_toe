# board
# show board
# play game
# handle turn
# check win
#     check vertical
#     check horizontal
#     check diagonal
# check tie
# switch player

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "x"


def display_board():

    print(f"    {board[6]}|{board[7]}|{board[8]}    [7|8|9]")
    print(f"    {board[3]}|{board[4]}|{board[5]}    [4|5|6]")
    print(f"    {board[0]}|{board[1]}|{board[2]}    [1|2|3]")


def game_start():

    display_board()

    while game_still_going:

        player_turn(current_player)

        check_game_over()

        flip_player()

    if winner == "x" or winner == "o":
        print("Player: " + (winner) + " Wins!")
    else:
        print("Its a Tie!")


def player_turn(player):

    print(f"  {player}'s Turn.")
    position = input("Player Choose Between 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Player Choose Between 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Already Taken!")

    board[position] = player
    display_board()


def check_game_over():

    check_if_win()
    check_if_tie()


def check_if_win():

    global winner

    row_winner = win_horizontal()
    column_winner = win_vertical()
    kona_winner = win_kona()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif kona_winner:
        winner = kona_winner
    else:
        winner = None


def win_horizontal():

    global game_still_going

    hori1 = board[6] == board[7] == board[8] != "-"
    hori2 = board[3] == board[4] == board[5] != "-"
    hori3 = board[0] == board[1] == board[2] != "-"

    if hori1 or hori2 or hori3:
        game_still_going = False

    if hori1:
        return board[6]
    elif hori2:
        return board[3]
    elif hori3:
        return board[0]


def win_vertical():
    global game_still_going

    vert1 = board[6] == board[3] == board[0] != "-"
    vert2 = board[7] == board[4] == board[1] != "-"
    vert3 = board[8] == board[5] == board[2] != "-"

    if vert1 or vert2 or vert3:
        game_still_going = False

    if vert1:
        return board[6]
    elif vert2:
        return board[7]
    elif vert3:
        return board[8]


def win_kona():

    global game_still_going

    kona1 = board[6] == board[4] == board[2] != "-"
    kona2 = board[8] == board[4] == board[0] != "-"

    if kona1 or kona2:
        game_still_going = False

    if kona1:
        return board[6]
    elif kona2:
        return board[8]


def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False


def flip_player():

    global current_player

    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
    return


print("Welcome To Tic-Tac-Toe!")
game_start()
print("Thanks For Playing!")
