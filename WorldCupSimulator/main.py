from window import Window
from scene import LoadingScreen, MainMenu, Game
import pygame

window = Window("World Cup Simulator", (960, 720))
loadingScreen = LoadingScreen(window, name="World Cup Simulator [Loading Screen]")
selectScreen = MainMenu(window, name="World Cup Simulator [Main Menu]")
gameScreen = Game(window, name="World Cup Simulator [Main Menu]")

window.RegisterScene(loadingScreen)
window.RegisterScene(selectScreen)
window.RegisterScene(gameScreen)
window.SetCurrentScene(0)

while window.running:
    window.MainLoop()
    pygame.display.flip()
