from pyray import *


class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawO(self):
        draw_ring((self.x, self.y), 40.0, 30.0, 0.0, 360.0, 0, BLACK)

    def drawX(self):
        c = 40
        draw_line_ex((self.x - c, self.y - c), (self.x + c, self.y + c), 5.0, BLACK)
        draw_line_ex((self.x + c, self.y - c), (self.x - c, self.y + c), 5.0, BLACK)
