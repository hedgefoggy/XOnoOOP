board_size = 3

board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    print("_ * 4 board_size")
    for i in range(board_size):
        print((" " * 3 + "|") * 3)
        print("", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2], "|")
        print(("_" * 3 + "|") * 3)
def game_step(index, char):
    if (index > 9 or index < 1 or board[index-1] in ("X", "O")):
        return False

    board[index - 1] = char
    return True

def check_win():
    win = False

    win_combination = ((0,1,2), (3,4,5), (6,7,8),   # horizontal
                       (0,3,6), (1,4,7), (2,5,8),   # vertical
                       (0,4,8), (2,4,6))            # diagonal

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def start_game():
    current_player = 'X'
    step = 1
    draw_board()

    while (step < 10) and (check_win() == False):
        index = int(input("Player move " + current_player + ". Input cell: (0 - exit) "))

        if (index == "0"):
            break

        #if took a step
        if(game_step(int(index), current_player)):
            print("The move is made")

            if (current_player == "X"):
                current_player = "O"
            else:
                current_player = "X"

            draw_board()
            step += 1
        else:
            print("Wrong move! Repeat!")

    if (step > 9):
        print("Dead heat!")
    else:
        print("Winner " + check_win())
start_game()