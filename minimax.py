AI = "X"
HUMAN = "O"

def check_3(a, b, c):
    return a == b and b == c and a != ""


def check_win(board):
    for i in range(0, 3):
        if check_3(board[0][i], board[1][i], board[2][i]):
            return board[0][i] 

    for i in range(0, 3):
        if check_3(board[i][0], board[i][1], board[i][2]):
            return board[i][0]

    if check_3(board[0][0], board[1][1], board[2][2]):
        return board[1][1] 

    if check_3(board[2][0], board[1][1], board[0][2]):
        return board[1][1] 

    if len(available_spots(board)) == 0:
        return "draw"
    else:
        return "wait"


def available_spots(board):
    available = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == "":
                available.append([i, j])
    return available

def best_move(board):
    best_score = -1000000
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == "":
                board[i][j] = AI
                score = minimax(HUMAN, board)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = [i, j]
    
    return move

scores = {
    "X": 10,
    "O": -10,
    "draw": 0
}

def minimax(player, board):
    result = check_win(board)
    if result != "wait":
        return scores[result]
    
    if player == AI:
        best_score = -1000000
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == "":
                    board[i][j] = AI
                    score = minimax(HUMAN, board)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        
        return best_score
    else:
        best_score = 1000000
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == "":
                    board[i][j] = HUMAN
                    score = minimax(AI, board)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        
        return best_score

