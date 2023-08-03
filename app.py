from pyray import *
from box import *
import random
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


def draw_screen():
    draw_line(100, 0, 100, 300, BLACK)
    draw_line(200, 0, 200, 300, BLACK)
    draw_line(0, 100, 300, 100, BLACK)
    draw_line(0, 200, 300, 200, BLACK)


def draw_board(board):
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == AI:
                space[count].drawX()
            elif board[i][j] == HUMAN:
                space[count].drawO()
            count += 1


def turn_change(turn):
    if turn == HUMAN:
        return AI
    else:
        return HUMAN


def equals3(a, b, c):
    return a == b and b == c and a != ""


def check_win(board):
    winner = 0
    for i in range(0, 3):
        if equals3(board[0][i], board[1][i], board[2][i]):
            return board[0][i] 

    for i in range(0, 3):
        if equals3(board[i][0], board[i][1], board[i][2]):
            return board[i][0]

    if equals3(board[0][0], board[1][1], board[2][2]):
        return board[1][1] 

    if equals3(board[2][0], board[1][1], board[0][2]):
        return board[1][1] 

    if len(available_spots(board)) == 0:
        return "draw"


def available_spots(board):
    available = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == "":
                available.append([i, j])
    return available


while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_screen()

    if turn == AI:
        available = available_spots(board)
        x, y  = random.choice(available)
        board[x][y] = AI
        turn = HUMAN

    draw_board(board)
    if is_mouse_button_pressed(0):
        pos = get_mouse_position()
        if pos.x < 100:
            if pos.y < 100:
                if board[0][0] == "":
                    board[0][0] = turn
                    turn = "X"
            elif pos.y < 200:
                if board[1][0] == "":
                    board[1][0] = turn
                    turn = "X"
            else:
                if board[2][0] == "":
                    board[2][0] = turn
                    turn = "X"
        elif pos.x < 200:
            if pos.y < 100:
                if board[0][1] == "":
                    board[0][1] = turn
                    turn = "X"
            elif pos.y < 200:
                if board[1][1] == "":
                    board[1][1] = turn
                    turn = "X"
            else:
                if board[2][1] == "":
                    board[2][1] = turn
                    turn = "X"
        else:
            if pos.y < 100:
                if board[0][2] == "":
                    board[0][2] = turn
                    turn = "X"
            elif pos.y < 200:
                if board[1][2] == "":
                    board[1][2] = turn
                    turn = "X"
            else:
                if board[2][2] == "":
                    board[2][2] = turn
                    turn = "X"


    draw_board(board)
    if check_win(board) == AI:
        draw_text("Player X won", 20, 120, 40, RED)
        turn = 0
    elif check_win(board) == HUMAN:
        draw_text("Player O won", 20, 120, 40, RED)
        turn = 0
    elif check_win(board) == "draw":
        draw_text("Draw", 60, 120, 40, RED) 
        turn = 0

    end_drawing()
close_window()
