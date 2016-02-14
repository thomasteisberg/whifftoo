import pygame
import sys

# Colors!
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

# Pygame init
pygame.init()
screen = pygame.display.set_mode((1000,1000))

def toscreen(x, y):
        return (x+500, y)

# test!
screen.fill(black)
points = [(0,0), (10,10)]
pygame.draw.lines(screen, red, False, points, 10)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
