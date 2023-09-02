from pyray import *
from box import *
from minimax import *

WIDTH, HEIGHT = 300, 300
init_window(WIDTH, HEIGHT, "TIC TAC TOE")

space = []
for i in range(50, 300, 100):
    for j in range(50, 300, 100):
        space.append(Box(j, i))

pos = Vector2()
board = [["", "", ""], ["", "", ""], ["", "", ""]]
HUMAN = "O"
AI = "X"
turn = HUMAN
num = 0


def draw_screen():
    draw_line(100, 0, 100, 300, BLACK)
    draw_line(200, 0, 200, 300, BLACK)
    draw_line(0, 100, 300, 100, BLACK)
    draw_line(0, 200, 300, 200, BLACK)


def draw_board():
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == AI:
                space[count].drawX()
            elif board[i][j] == HUMAN:
                space[count].drawO()
            count += 1


while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_screen()

    if turn == AI:
        move = best_move(board)
        board[move[0]][move[1]] = AI
        turn = HUMAN

    draw_board()
    if is_mouse_button_pressed(0):
        pos = get_mouse_position()
        if pos.x < 100:
            if pos.y < 100:
                if board[0][0] == "":
                    board[0][0] = turn
                    turn = AI
            elif pos.y < 200:
                if board[1][0] == "":
                    board[1][0] = turn
                    turn = AI
            else:
                if board[2][0] == "":
                    board[2][0] = turn
                    turn = AI
        elif pos.x < 200:
            if pos.y < 100:
                if board[0][1] == "":
                    board[0][1] = turn
                    turn = AI
            elif pos.y < 200:
                if board[1][1] == "":
                    board[1][1] = turn
                    turn = AI
            else:
                if board[2][1] == "":
                    board[2][1] = turn
                    turn = AI
        else:
            if pos.y < 100:
                if board[0][2] == "":
                    board[0][2] = turn
                    turn = AI
            elif pos.y < 200:
                if board[1][2] == "":
                    board[1][2] = turn
                    turn = AI
            else:
                if board[2][2] == "":
                    board[2][2] = turn
                    turn = AI


    if check_win(board) == AI:
        draw_text("Player X won", 20, 120, 40, RED)
        turn = 0
    elif check_win(board) == HUMAN:
        draw_text("Player O won", 20, 120, 40, RED)
        turn = 0
    elif check_win(board) == "draw":
        draw_text("Draw", 100, 120, 40, RED) 
        turn = 0

    end_drawing()
close_window()
