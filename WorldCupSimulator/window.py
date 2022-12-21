import pygame
from scene import Scene
pygame.font.init()

# Window class. Handles some events and drawing entities. 
class Window:
    def __init__(self, name:str="New Window", size:tuple=(700,700)):
        self.name = name
        self.size = pygame.Vector2(size[0], size[1])
        self.background_colour = (53, 53, 53)

        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True

        self.scenes = []
        self.currentScene = None

    def RegisterScene(self, s:Scene):
        self.scenes.append(s)

    def RemoveScene(self, s:Scene):
        self.scenes.remove(s)
    
    def SetCurrentScene(self, s:int):
        self.currentScene = self.scenes[s]
        
    def MainLoop(self):
        pygame.display.set_caption(self.name)
        self.clock.tick(60)
        self.screen.fill(self.background_colour)

        self.currentScene.Update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def Text(self, msg:str, position:tuple, color:tuple=(255,255,255), size:int=50, alpha:int=255):
        font = pygame.font.Font("Assets/font/Font.ttf", size)
        text = font.render(msg, True, color)

        text.set_alpha(alpha)

        rect = text.get_rect()

        rect.center = position

        self.screen.blit(text, rect)
