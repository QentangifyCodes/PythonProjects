from screen import *
import random

class RainDrop:
    def __init__(self):
        self.position = pygame.Vector2(0, 0)
        self.speed = 0
        self.Reset()
    
    def Draw(self):
        pygame.draw.ellipse(screen, (255,255,255), (self.position.x, self.position.y, 5, 10))
    
    def Reset(self):
        self.position.y = -10
        self.position.x = random.randint(0, size[0])
        self.speed = random.randint(10, 20)

    def Update(self):
        self.Draw()
        self.position.y += self.speed

        if self.position.y > size[1]:
            self.Reset()

class RainBackground:
    def __init__(self):
        self.rainDrops = []
        self.GenerateRainDrops()
    
    def GenerateRainDrops(self):
        for x in range(100):
            self.rainDrops.append(RainDrop())
    
    def Update(self):
        for raindrop in self.rainDrops:
            raindrop.Update()