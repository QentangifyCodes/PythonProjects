from stupidWorld import *
import random


seed = random.randint(0, 100)
grid = World(0.01, seed)

while running:
    screen.fill(background_colour)
    grid.Update()
    Text(f"Seed: {seed}", (10, 670), (0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
