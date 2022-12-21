from window import Window
from grid import Grid
import pygame

window = Window("World Simulator", (1000, 1000))
entity = Grid(window)

while window.running:
    window.MainLoop()
    pygame.display.flip()
