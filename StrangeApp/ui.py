from screen import *
import os
import Application

class Button:
    def __init__(self, position:tuple, size:tuple, text:str):
        self.position = position

        self.size = list(size)
        self.currentSize = list(size)

        self.sprite = pygame.image.load("Assets/Sprites/Button.png")
        self.rect = self.sprite.get_rect()
        self.rect.center = self.position

        self.text = text
        self.textObject = None
        self.textRect = None

        self.pressed = False

    def Draw(self):
        # Updating the scale of the sprite and the rect
        sprite = pygame.transform.scale(self.sprite, self.currentSize)
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.currentSize[0], self.currentSize[1])
        self.rect.center = self.position

        #Drawing sprite
        screen.blit(sprite, self.rect)

        # Updating the width of the text and drawing it
        self.FitText()
        screen.blit(self.textObject, self.textRect)

    def FitText(self):
        # KINDA MESSY. Decreasing font size until it fits into the box with a little offset
        size = 70
        font = pygame.font.Font(f"Assets/Fonts/Font.ttf",  size)
        text = font.render(self.text, (255,255,255), True)
        
        while text.get_rect().width>self.rect.width-self.rect.width/7:
            font = pygame.font.Font(f"Assets/Fonts/Font.ttf", size)
            text = font.render(self.text, (255,255,255), True)
            size-=1

        # Moving the text to  the center  of the box
        rect = text.get_rect()
        rect.center = self.rect.center

        self.textObject = text
        self.textRect = rect

    def Interact(self):
        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            # True if being pressed
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                self.pressed = False

            # Selected indicator 
            if self.currentSize[0]<self.size[0]+10:
                self.currentSize[0] += 2.5
            if self.currentSize[1]<self.size[1]+10:
                self.currentSize[1] += 2.5

            pygame.draw.rect(screen, (0, 0, 0), (self.rect.x-6, self.rect.y-6, self.rect.width+12, self.rect.height+12))
            pygame.draw.rect(screen, (255, 255, 255), (self.rect.x-4, self.rect.y-4, self.rect.width+8, self.rect.height+8))

        else:
            # Resetting the size
            if self.currentSize[0]>self.size[0]:
                self.currentSize[0] -= 2.5
            if self.currentSize[1]>self.size[1]:
                self.currentSize[1] -= 2.5

    def Update(self):
        self.Interact()
        self.Draw()

# Text that fades in after a few frames
class FadeInText:
    def __init__(self, text:str, center:tuple=(350, 250), size:int=50, rate:int=1):
        self.text = text
        self.center = center
        self.size = size

        self.rate = rate
        self.alpha = 0
    
    def Draw(self):
        Text(self.text, self.center, size=self.size, alpha=int(self.alpha))

    def Update(self):
        self.Draw()

        # Increasing alpha untill max alpha
        if self.alpha<255:
            self.alpha+=self.rate

class FadeEffect:
    def __init__(self, direction:int=1, speed:int=5):
        self.square = pygame.Surface((700, 500))
        self.background = None
        
        self.speed = speed # How fast to fade in or out

        # True if done fading or is currently fading
        self.done = False
        self.fading = False

        # Checking whether to fade out or fade in
        self.direction = direction
        self.alpha =  0

        if self.direction == -1:
            self.alpha = 250

    def Draw(self):
        square = self.square
        square.set_alpha(self.alpha)
        screen.blit(square, (0,0))
    
    def Update(self):
        self.background = pygame.image.save(screen, "temp.png")
        self.background = pygame.image.load("temp.png")

        while not self.done:
            screen.blit(self.background, (0,0))
            clock.tick(60)
            self.Draw()

            if not self.done:
                self.Fade()
                        
            pygame.display.flip()
        os.remove("temp.png")

    def Fade(self):
        # Increasing or decreasing alpha nutil it reaches 250 or 0
        if (self.direction==1 and self.alpha >= 255) or (self.direction==-1 and self.alpha <= 0):
            self.done = True
            self.fading = False
            return

        self.alpha += self.direction*self.speed
        self.fading = True

class ApplicationSelector:
    def __init__(self):
        self.applications = [
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App(),
            Application.App()        
        ]

        self.selectionSquares = []

        x, y = 35, 100
        for app in self.applications:
            if x+160>700:
                y+=160
                x=35
            rect = pygame.Rect(x,y,150, 150)

            self.selectionSquares.append(Application.SeletorSquare(rect, app))
            x+=160


    def Update(self):
        for square in self.selectionSquares:
            square.Update()
