"""
Conway's Game of Life Rules
1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2.Any live cell with two or three live neighbours lives on to the next generation.
3.Any live cell with more than three live neighbours dies, as if by overpopulation.
4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

1 = DEAD SQUARE
0 = ALIVE Square
"""
import pygame
import MyRec
import random


class Grid:

    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height / scale)
        self.rows = int(width / scale)
        self.offset = offset
        self.width = width
        self.height = height
        self.board = [0]*10
        for i in range(10):
            self.board[i] = [0]*10
        self.change = []

    def draw_squares(self, foreground, surface):
        x = 0
        y = 0
        random.seed(241)
        for x_pos in range(0, self.width, self.scale + self.offset):
            for y_pos in range(0, self.height, self.scale + self.offset):
                # pygame.draw.rect(surface, foreground, pygame.Rect(x_pos, y_pos, self.scale, self.scale),  0)
                self.board[x][y] = MyRec.MyRec(x_pos, y_pos, self.scale, self.scale, 1)
                y += 1
            x += 1
            y = 0
        self.board[1][1].seton(0)
        self.board[1][2].seton(0)
        self.board[1][3].seton(0)

    def move(self):
        for x in range(10):
            for y in range(10):
                nCount = 0  # NEIGHBOR COUNT
                #  getncount(x, y)
                #  START GET N COUNT LOGIC ** THIS SHOULD BE A FUNCTION **
                if x == 0 and y == 0:  # TOP LEFT CORNER LOGIC
                    if self.board[x+1][y+1].geton() == 1:
                            nCount += 1
                    if self.board[x][y+1].geton() == 1:
                            nCount += 1
                    if self.board[x+1][y].geton() == 1:
                            nCount += 1
                elif x == 9 and y == 0:  # BOT LEFT CORNER LOGIC
                    if self.board[x-1][y].geton() == 1:
                            nCount += 1
                    if self.board[x][y+1].geton() == 1:
                            nCount += 1
                    if self.board[x-1][y+1].geton() == 1:
                            nCount += 1
                elif x == 0 and y == 9:  # TOP RIGHT CORNER LOGIC
                    if self.board[x][y-1].geton() == 1:
                            nCount += 1
                    if self.board[x+1][y].geton() == 1:
                            nCount += 1
                    if self.board[x+1][y-1].geton() == 1:
                            nCount += 1
                elif x == 9 and y == 9:  # BOT RIGHT CORNER LOGIC
                    if self.board[x][y-1].geton() == 1:
                            nCount += 1
                    if self.board[x-1][y].geton() == 1:
                            nCount += 1
                    if self.board[x-1][y-1].geton() == 1:
                            nCount += 1
                elif x == 0 or y == 0 or x == 9 or y == 9:  # LOGIC FOR EDGE OF BOARD
                    if y == 0:  # LEFT SIDE OF BOARD
                        if self.board[x+1][y].geton() == 1:
                            nCount += 1
                        if self.board[x-1][y].geton() == 1:
                            nCount += 1
                        if self.board[x][y+1].geton() == 1:
                            nCount += 1
                        if self.board[x+1][y+1].geton() == 1:
                            nCount += 1
                        if self.board[x-1][y+1].geton() == 1:
                            nCount += 1
                    if x == 0:  # TOP OF THE BOARD LOGIC
                        if self.board[x][y+1].geton() == 1:
                            nCount += 1
                        if self.board[x][y-1].geton() == 1:
                            nCount += 1
                        if self.board[x+1][y].geton() == 1:
                            nCount += 1
                        if self.board[x+1][y+1].geton() == 1:
                            nCount += 1
                        if self.board[x+1][y-1].geton() == 1:
                            nCount += 1
                    if y == 9:  # RIGHT SIDE OF BOARD LOGIC
                        if self.board[x+1][y].geton() == 1:
                            nCount += 1
                        if self.board[x-1][y].geton() == 1:
                            nCount += 1
                        if self.board[x][y-1].geton() == 1:
                            nCount += 1
                        if self.board[x-1][y-1].geton() == 1:
                            nCount += 1
                        if self.board[x+1][y-1].geton() == 1:
                            nCount += 1
                    if x == 9:  # BOTTOM OF BOARD LOGIC
                        if self.board[x][y+1].geton() == 1:
                            nCount += 1
                        if self.board[x][y-1].geton() == 1:
                            nCount += 1
                        if self.board[x-1][y].geton() == 1:
                            nCount += 1
                        if self.board[x-1][y-1].geton() == 1:
                            nCount += 1
                        if self.board[x-1][y+1].geton() == 1:
                            nCount += 1
                else:  # ALL NON SPECIAL CASES LOGIC
                    if self.board[x-1][y].geton() == 2:
                        nCount += 1
                    if self.board[x+1][y].geton() == 2:
                        nCount += 1
                    if self.board[x][y-1].geton() == 2:
                        nCount += 1
                    if self.board[x][y+1].geton() == 2:
                        nCount += 1
                    if self.board[x+1][y+1].geton() == 2:
                        nCount += 1
                    if self.board[x-1][y-1].geton() == 2:
                        nCount += 1
                    if self.board[x+1][y-1].geton() == 2:
                        nCount += 1
                    if self.board[x-1][y+1].geton() == 2:
                        nCount += 1
                # END GET N COUNT LOGIC
                if self.board[x][y].geton() == 0:  # LIVE CELL
                    if nCount > 3:  # DIES TO OVER POP
                        self.change.append([x, y, 1])  # 1 for dead cell
                    if nCount < 2:  # DIES TO UNDER POP
                        self.change.append([x, y, 1])  # 1 for dead cell
                if self.board[x][y].geton() == 1:  # DEAD CELL
                    if nCount == 3:  # CELL REGENERATES
                        self.change.append([x, y, 0])  # 0 for alive cell

    def makechange(self):
        for i in self.change:  # Getting instructions in sets of 3 from a list so all changes happen together in one generation
            self.board[i[0]][i[1]].seton(i[2])

    def draw(self, surface, foreground):
        for x in range(10):
            for y in range(10):
                pygame.draw.rect(surface, foreground, pygame.Rect(self.board[x][y].getxpos(), self.board[x][y].getypos(), self.scale, self.scale),  self.board[x][y].geton())
"""
makechange function is hacky code to fix problem with changing squares one by one as we iterate through board.
changing squares before looking at how that affects other squares was breaking. So now we iterate
through all squares, note changes in list, then apply all the changes in makechange before printing
"""
