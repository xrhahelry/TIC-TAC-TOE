from pyray import *
from box import *

WIDTH, HEIGHT = 300, 300
init_window(WIDTH, HEIGHT, "TIC TAC TOE")

space = []
for i in range(50, 300, 100):
    for j in range(50, 300, 100):
        space.append(Box(j, i))

pos = Vector2()
board = [2, 2, 2, 2, 2, 2, 2, 2, 2]
l = len(space)
turn = 0


def draw_screen():
    draw_line(100, 0, 100, 300, BLACK)
    draw_line(200, 0, 200, 300, BLACK)
    draw_line(0, 100, 300, 100, BLACK)
    draw_line(0, 200, 300, 200, BLACK)


def draw_board(board):
    count = 0
    for i in board:
        if i != 2:
            if i == 1:
                space[count].drawX()
            else:
                space[count].drawO()
        count += 1


def turn_change(turn):
    if turn == 0:
        return 1
    else:
        return 0


def check_win(board):
    if (
        ((board[0] == board[1] and board[1] == board[2]) and board[0] != 2)
        or ((board[3] == board[4] and board[4] == board[5]) and board[3] != 2)
        or ((board[6] == board[7] and board[7] == board[8]) and board[6] != 2)
    ):
        return True
    elif (
        ((board[0] == board[3] and board[3] == board[6]) and board[0] != 2)
        or ((board[1] == board[4] and board[4] == board[7]) and board[1] != 2)
        or ((board[2] == board[5] and board[5] == board[8]) and board[2] != 2)
    ):
        return True
    elif ((board[0] == board[4] and board[4] == board[8]) and board[0] != 2) or (
        (board[2] == board[4] and board[4] == board[6]) and board[2] != 2
    ):
        return True
    else:
        return False


while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_screen()
    
    if check_win(board):
        draw_board(board)
        if turn == 1:
            draw_text("Player O won", 20, 120, 40, RED)
        else:
            draw_text("Player X won", 20, 120, 40, RED)
    else:
        draw_board(board)
        if is_mouse_button_pressed(0):
            pos = get_mouse_position()
            if pos.x < 100:
                if pos.y < 100:
                    if board[0] == 2:
                        board[0] = turn
                        turn = turn_change(turn)
                elif pos.y < 200:
                    if board[3] == 2:
                        board[3] = turn
                        turn = turn_change(turn)
                else:
                    if board[6] == 2:
                        board[6] = turn
                        turn = turn_change(turn)
            elif pos.x < 200:
                if pos.y < 100:
                    if board[1] == 2:
                        board[1] = turn
                        turn = turn_change(turn)
                elif pos.y < 200:
                    if board[4] == 2:
                        board[4] = turn
                        turn = turn_change(turn)
                else:
                    if board[7] == 2:
                        board[7] = turn
                        turn = turn_change(turn)
            else:
                if pos.y < 100:
                    if board[2] == 2:
                        board[2] = turn
                        turn = turn_change(turn)
                elif pos.y < 200:
                    if board[5] == 2:
                        board[5] = turn
                        turn = turn_change(turn)
                else:
                    if board[8] == 2:
                        board[8] = turn
                        turn = turn_change(turn)

    end_drawing()
close_window()
