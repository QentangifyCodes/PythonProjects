from screen import *

class Blob:
    def __init__(self):
        self.sprite = pygame.image.load("res/Circle.png")
        self.rect = self.sprite.get_rect()
        self.position = pygame.Vector2(size[0]/2, size[1]/2)

        self.clicks = 0

        # Goofy Click Effect
        self.alpha = 255
        self.size = 125
        self.currentSize = self.size
        self.effectSpeed = 5
        self.increasing = False
        self.decreasing = False
        self.effect = False

    def Draw(self):
        sprite = pygame.transform.smoothscale(self.sprite, (self.currentSize, self.currentSize))
        sprite.set_alpha(self.alpha)
        self.rect = sprite.get_rect()
        self.rect.center = self.position
        screen.blit(sprite, self.rect)

        Text(str(self.clicks), (size[0]/2, 100))
    
    def ClickEffect(self):
        if not self.effect:
            return

        if self.decreasing and self.size >= self.currentSize:
            self.effect = False
            self.increasing = False
            self.decreasing = False
            self.alpha = 255
            return
        
        if int(self.currentSize) <= self.size:
            self.increasing = True
        elif int(self.currentSize) >= self.size*1.2:
            self.decreasing = True

        if self.increasing and not self.decreasing:
            self.currentSize+= self.effectSpeed
        if self.decreasing:
            self.currentSize -= self.effectSpeed
        self.alpha -= 5

    def Click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.effect = True
            self.clicks += 1
            
    def Update(self):
        self.Draw()
        self.ClickEffect()