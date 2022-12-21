from window import Window
from tournament import Tournament, loadTeams
import pygame

window = Window("World Cup Simulator", (960, 720))
t = Tournament(window, loadTeams())

while window.running:
    window.MainLoop()
    t.Update()
    pygame.display.flip()
