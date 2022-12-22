import pygame, random
from gameobject import Gameobject

# loading all teams from a text file
def loadTeams():
    with open("Assets/teams.txt", "r") as f:
        lines = f.readlines()

    teams = []
    for line in lines:
        teams.append(line.strip())
    # Generating teams that qualified
    count = 0
    qualifiedTeams = []
    for i in range(len(teams)):
        if 50>random.randint(0, 100):
            qualifiedTeams.append(teams[i])
            count+=1

            
        if count==16:
            break
    return qualifiedTeams

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
            
class Text(Gameobject):
    def __init__(self, scene, msg:str, position:tuple, color:tuple=(255,255,255), size:int=50):
        super().__init__(scene)
        self.msg = msg
        self.position = pygame.Vector2(position[0], position[1])
        self.color = color
        self.size = size
    
    def Draw(self):
        self.scene.window.Text(self.msg, self.position, self.color, self.size)

class FadeInText(Text):
    def __init__(self, scene, msg: str, position: tuple, color: tuple = (255, 255, 255), size: int = 50):
        super().__init__(scene, msg, position, color, size)
        self.alpha = 0

    def Draw(self):
        self.scene.window.Text(self.msg, self.position, self.color, self.size, self.alpha)

    def Update(self):
        self.Draw()
        if self.alpha < 255:
            self.alpha+=1

class LoadingBar(Gameobject):
    def __init__(self, scene, position:tuple):
        super().__init__(scene)
        self.width = 0
        self.position = position

        self.text = FadeInText(scene, "Press SPACE to continue", (self.scene.window.size.x/2, self.scene.window.size.y/2+50), size=30)

        self.completed = False
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, 50)

        self.soccer = pygame.transform.scale(pygame.image.load("Assets/images/LoadingSoccerBall.png"), (50,50))
    
    def Draw(self):
        self.rect.width = self.width
        pygame.draw.rect(self.scene.window.screen, (255, 255, 255), self.rect)
    
    def Update(self):
        self.Draw()

        if self.width>self.scene.window.size.x-100:
            self.completed = True
            self.text.Update()
        else:
            self.width += random.randint(2, 10)

        if self.completed:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.scene.fadeOut = True
        
        self.scene.window.screen.blit(self.soccer, (self.position[0]+self.width-50, self.position[1]))

class Button(Gameobject):
    def __init__(self, scene, position:tuple, purpose, text:str, size:tuple = (208, 81), textSize:int=30):
        super().__init__(scene)

        self.position = position
        self.size = list(size)
        self.normalSize = size
        self.text = text
        self.textSize = textSize

        self.purpose = purpose

        self.sprite = pygame.image.load("Assets/images/Button.png")
        self.rect = self.sprite.get_rect()
        self.pressed = False

    def Draw(self):
        sprite = pygame.transform.smoothscale(self.sprite, self.size)

        self.rect = sprite.get_rect()
        self.rect.center = self.position
        self.scene.window.screen.blit(sprite, self.rect)
        self.scene.window.Text(self.text, self.rect.center, size=self.textSize)
    
    def HoverEffect(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.sprite.set_alpha(100)
            if self.size[0] <  self.normalSize[0] + 30 and self.size[1] <  self.normalSize[1] + 30 :
                self.size[0] += 5
                self.size[1] += 5  
                self.textSize+= 2
            
            if pygame.mouse.get_pressed()[0]:
                self.purpose(self)
        else:
            self.sprite.set_alpha(75)
            if self.size[0] > self.normalSize[0] and self.size[1] >  self.normalSize[1]:
                self.size[0] -= 5
                self.size[1] -= 5  
                self.textSize-= 2
                
    def Update(self):
        self.HoverEffect()
        self.Draw()

class ListUi(Gameobject):
    def __init__(self, scene, name:str,  position:tuple):        
        super().__init__(scene)
        self.items = loadTeams()
        self.name = name
        self.position = position
        self.refreshTime = 0
        self.refreshAmount = 0

    def refresh(self):
        if self.refreshTime <= 0:
            self.items = loadTeams()
            self.refreshTime = 1
            self.refreshAmount += 1
        else:
            self.refreshTime -= 0.09
        

    
    def Draw(self):
        self.scene.window.Text(self.name+"[%d]"%self.refreshAmount, (self.position[0]+125, self.position[1]-15), size=20)

        posx = self.position[0] - 20
        c = 0
        for i in range(8):
            for x in range(2):
                rect = pygame.Rect(posx+130*x, self.position[1]+i*65, 125, 60)
                pygame.draw.rect(self.scene.window.screen, (0,0,0), rect)
                self.scene.window.Text(self.items[c], rect.center, size=15)
                c+=1
            
