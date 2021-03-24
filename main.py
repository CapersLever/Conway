"""
Conway's Game of Life Rules
1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2.Any live cell with two or three live neighbours lives on to the next generation.
3.Any live cell with more than three live neighbours dies, as if by overpopulation.
4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
import pygame
import os
import grid


os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 1000, 1000  # screen size
size = (width+500, height)

pygame.init()
pygame.display.set_caption("Conway's Game Of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
green = (0, 200, 0)
white = (255, 255, 255)
blue = (0, 14, 71)

scale = 100
offset = 1

nextbutton = pygame.Rect(1050, 50, 70, 40)  # (x, y, width, height)
smallFont = pygame.font.SysFont('Corbel', 35)
text = smallFont.render('Next', True, white)

quitbutton = pygame.Rect(1050, 110, 70, 40)
quitText = smallFont.render('Quit', True, white)

Grid = grid.Grid(width, height, scale, offset)
run = True
Grid.draw_squares(green, screen)
while run:
    clock.tick(fps)
    screen.fill(black)
    pygame.draw.rect(screen, blue, nextbutton)
    pygame.draw.rect(screen, blue, quitbutton)
    screen.blit(text, (1053, 53))  # Next Button Text
    screen.blit(quitText, (1053, 113))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos  # GETS MOUSE POSITION
            if nextbutton.collidepoint(mousePos):
                Grid.move()
            if quitbutton.collidepoint(mousePos):
                pygame.quit()
    Grid.makechange()
    Grid.draw(screen, green)
    pygame.display.update()
pygame.quit()

