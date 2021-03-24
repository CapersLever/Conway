import pygame


class MyRec:
    def __init__(self, x_pos, y_pos, width, height, on):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.on = on

    def getxpos(self):
        return self.x_pos

    def getypos(self):
        return self.y_pos

    def geton(self):
        return self.on

    def seton(self, value):
        self.on = value
