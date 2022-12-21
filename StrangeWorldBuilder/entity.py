import pygame

entities = [] # list with all entities in the program

# Base Class for all entities
class Entity():
    def __init__(self):
        entities.append(self)

    def Draw(self):
        pass

    def Update(self):
        pass

# Any Drawable Entity
class Sprite(Entity):
    def __init__(self, window, position:tuple, sprite:str=None):
        self.window = window
        self.sprite = pygame.Surface((50, 50))
        self.sprite.fill((0,0,0))
        
        if sprite != None:
            self.sprite = pygame.image.load(sprite)

        self.rect = self.sprite.get_rect()

        self.position = pygame.Vector2(position[0], position[1])

        super().__init__()

    def Draw(self):
        self.window.screen.blit(self.sprite, self.rect)

    def Update(self):
        self.rect.topleft = self.position
        self.Draw()