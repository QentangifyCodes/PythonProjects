from importlib.machinery import ModuleSpec
import pygame, utils


class NumButton:
    def __init__(self, position:tuple, character:str, color1=(32, 51, 51), color2=(57, 91, 100)):
        self.screen = utils.screen
        self.rect = pygame.Rect(position[0], position[1], 100, 50)
        self.character = character

        self.color1 = color1
        self.color2 = color2

        self.currentColors = [self.color1, self.color2]
        self.hovering = False
    
    def Draw(self):
        pygame.draw.rect(self.screen, self.currentColors[0], self.rect)

        middle = pygame.Rect(0,0,self.rect.width-10, self.rect.height-10)
        middle.center = self.rect.center

        pygame.draw.rect(self.screen, self.currentColors[1], middle)

        utils.DrawText(self.character, self.rect.center)
    
    def ListenForClicks(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if not self.hovering:
                darkAmt = (20,20,20)
                self.currentColors[0] = (self.currentColors[0][0]-darkAmt[0], self.currentColors[0][1]-darkAmt[1], self.currentColors[0][2]-darkAmt[0])
                self.currentColors[1] = (self.currentColors[1][0]-darkAmt[0], self.currentColors[1][1]-darkAmt[1], self.currentColors[1][2]-darkAmt[0])
                self.hovering = True
        else:
            self.currentColors[0] = self.color1
            self.currentColors[1] = self.color2
            self.hovering = False



    def Update(self):
        self.ListenForClicks()
        self.Draw()

class OppButton(NumButton):
    def __init__(self, position: tuple, character: str):
        super().__init__(position, character, (32, 37, 37), (27, 32, 32))