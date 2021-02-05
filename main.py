import pygame,random
from pygame.locals import *
pygame.init()
# colors
grey = (117,120,118)

# global variable
screen_width,screen_height = 800,600
fps = 40
run = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("carGame")


while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    screen.fill(grey)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
exit()