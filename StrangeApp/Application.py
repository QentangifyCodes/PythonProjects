from types import MethodType
from screen import *

# Container for all the apps
class App:
    def __init__(self, name:str="Untitled", Main:MethodType=None, image:pygame.Surface=None) -> None:
        self.name = name
        self.main = Main
        self.image = image

# The class for the squares in the application selector
class SeletorSquare:
    def __init__(self, rect:pygame.Rect, app:App):
        self.rect= rect
        self.app = app

        # Needed to display the text name
        self.textRect = pygame.Rect
        self.text = pygame.Surface

        self.FitText()

    def FitText(self):
        # KINDA MESSY. Decreasing font size until it fits into the box with a little offset
        size = 50
        font = pygame.font.Font(f"Assets/Fonts/TitleFont.ttf", size)
        text = font.render(self.app.name, (255,255,255), True)
        
        while text.get_rect().width>self.rect.width-20:
            font = pygame.font.Font(f"Assets/Fonts/TitleFont.ttf", size)
            text = font.render(self.app.name, (255,255,255), True)
            size-=1

        # Moving the text to  the center bottom of the box
        rect = text.get_rect()
        rect.bottom = self.rect.bottom
        rect.centerx = self.rect.centerx

        self.textRect = rect    
        self.text = text

    def Draw(self):
        pygame.draw.rect(screen, (50,50,50), self.rect)
        screen.blit(self.text, self.textRect)

    def Update(self):
        self.CheckForSelection()
        self.Draw()

    def CheckForSelection(self):
        # Launching the app if pressed. 
        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            # Selected indicator 
            pygame.draw.rect(screen, (0,0,0), (self.rect.x-10, self.rect.y-10, self.rect.width+20, self.rect.height+20))
            pygame.draw.rect(screen, (255,255,255), (self.rect.x-5, self.rect.y-5, self.rect.width+10, self.rect.height+10))