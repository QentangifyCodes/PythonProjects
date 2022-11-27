from utils import *
from grid import Grid


running = True
t = Grid(30)

while running:
    pygame.display.set_caption(f'Conways Game of Life <Gen {t.generations}>')
    clock.tick(200)
    screen.fill(background_colour)

    if not t.started:
        t.EditMode()
    else:
        t.Update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
