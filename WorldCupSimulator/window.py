import pygame
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

        pygame.display.set_caption(self.name)

    
    def MainLoop(self):
        self.clock.tick(60)
        self.screen.fill(self.background_colour)

        self.Text("World Cup 2024", (self.size.x/2, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def Text(self, msg:str, position:tuple, color:tuple=(255,255,255), size:int=50):
        font = pygame.font.SysFont(None, size)
        text = font.render(msg, True, color)

        rect = text.get_rect()

        rect.center = position

        self.screen.blit(text, rect)
