import pygame
from entity import Entity, entities

# Window class. Handles some events and drawing entities. 
class Window:
    def __init__(self, name:str="New Window", size:tuple=(700,700)):
        self.name = name
        self.size = pygame.Vector2(size[0], size[1])
        self.background_colour = (135, 206, 235)

        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_caption(self.name)

    
    def MainLoop(self):
        self.clock.tick(60)
        self.screen.fill(self.background_colour)

        for entity in entities:
            entity.Update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
