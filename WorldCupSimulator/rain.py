import random, pygame
from gameobject import Gameobject

class RainDrop:
    def __init__(self, scene):
        self.scene = scene
        self.position = pygame.Vector2(0, 0)
        self.speed = 0
        self.Reset()
    
    def Draw(self):
        pygame.draw.ellipse(self.scene.window.screen, (63, 77, 83), (self.position.x, self.position.y, 5, 10))
    
    def Reset(self):
        self.position.y = -10
        self.position.x = random.randint(0, self.scene.window.size.x)
        self.speed = random.randint(10, 20)

    def Update(self):
        self.Draw()
        self.position.y += self.speed

        if self.position.y > self.scene.window.size.y:
            self.Reset()

class RainBackground(Gameobject):
    def __init__(self, scene, rate:int):
        super().__init__(scene)
        self.rate = rate
        self.rainDrops = []
        self.GenerateRainDrops()

    def GenerateRainDrops(self):
        for x in range(self.rate):
            self.rainDrops.append(RainDrop(self.scene))
    
    def Update(self):
        for raindrop in self.rainDrops:
            raindrop.Update()