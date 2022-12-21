from gameobject import *
from rain import RainBackground
from tournament import *
import sys

class Scene:
    def __init__(self, window, bg:tuple=(23,23,23), name:str=None, nextScene:int=1):
        self.window = window
        self.gameobjects = []
        self.window.background_colour = bg
        self.window.name = name

        self.nextScene = nextScene
        self.alpha = 255
        self.fadeOut = False
        self.fadedIn = False

    def AddObject(self, object:Gameobject):
        self.gameobjects.append(object)
    
    def RemoveObject(self, object:Gameobject):
        self.gameobjects.remove(object)

    def FadeOut(self):
        surf = pygame.Surface((self.window.size.x, self.window.size.y))
        surf.fill((0,0,0))
        surf.set_alpha(abs(self.alpha))

        self.alpha += 5

        if self.alpha == 255:
            self.window.SetCurrentScene(self.nextScene)
        
        self.window.screen.blit(surf, (0,0))

    def FadeIn(self):
        surf = pygame.Surface((self.window.size.x, self.window.size.y))
        surf.fill((0,0,0))
        surf.set_alpha(self.alpha)

        self.alpha -= 5

        if self.alpha == 0:
            self.fadedIn = True
        
        self.window.screen.blit(surf, (0,0))
    
    def GetObject(self, t:object, index:int=0):
        objects = []
        for object in self.gameobjects:
            if t == type(object):
                objects.append(object)
        
        return objects[index]

    def Update(self):
        for gameobject in self.gameobjects:
            gameobject.Update()
        
        if not self.fadedIn:
            self.FadeIn()
            
        if self.fadeOut:
            self.FadeOut()

class LoadingScreen(Scene):
    def __init__(self, window, bg: tuple = (23, 23, 23), name: str = None):
        super().__init__(window, bg, name)

        self.AddObject(RainBackground(self, 500))
        self.AddObject(LoadingBar(self, (50, self.window.size.y-50)))
        self.AddObject(Text(self, "Sad Boy Productions presents..", (self.window.size.x/2, self.window.size.y/2)))

    def Update(self):
        super().Update()

class MainMenu(Scene):
    def __init__(self, window, bg: tuple = (23, 23, 23), name: str = None):
        super().__init__(window, bg, name, 2)

        # Button behaviours
        def Quit(gameobject):
            sys.exit()

        def Play(gameobject):
            gameobject.scene.fadeOut = True

        def Main(gameobject):
            gameobject.scene.GetObject(ListUi).refresh()

        self.AddObject(Button(self, (140, self.window.size.y/2), Main, "Requalify", (258, 111)))
        self.AddObject(Button(self, (140, self.window.size.y/2+100), Play, "Start", (258, 111)))
        self.AddObject(Button(self, (140, self.window.size.y/2+200), Quit, "Quit", (258, 111)))
        self.AddObject(Text(self, "World Cup Simulator", (self.window.size.x/2, 80), size=70))
        self.AddObject(RainBackground(self, 200))
        self.AddObject(ListUi(self, "Qualified Teams", (self.window.size.x-275, 160)))

class Game(Scene):
    def __init__(self, window, bg: tuple = (23, 23, 23), name: str = None):
        super().__init__(window, bg, name)

        def restart(gameobject):
            self.window.SetCurrentScene(1)
            self.window.currentScene.__init__(self.window, name="World Cup Simulator [Main Menu]")

        self.AddObject(Tournament(self.window))
        self.AddObject(Button(self, (self.window.size.x/2, 20), restart, "restart", size=(104, 40.5)))

    def Update(self):
        self.GetObject(Tournament).GenerateMatches(self.window.scenes[1].GetObject(ListUi).items)
        super().Update()
