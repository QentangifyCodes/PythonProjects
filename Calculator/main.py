import pygame, calculator
from utils import *

c = calculator.Calculator()

running = True
while running:
    screen.fill(background_color)
    c.Update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
