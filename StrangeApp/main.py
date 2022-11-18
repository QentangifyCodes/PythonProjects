from screen import *
import ui, background

# Fake loading screen to seem cool LMAO
def LoadingScreen():    
    text = ui.FadeInText("Presenting Bored Applications™", (350, 230), rate=3)
    text2 = ui.FadeInText("Press space", (350, 280), size=40)

    bar = background.FakeLoadingBar()
    backdrop = background.DotBackground() # Falling dots

    while True:
        clock.tick(60)
        screen.fill(background_colour)

        # Drawing and updating everything
        backdrop.Update()
        text.Update()
        bar.Update()
        
        # After the fake loading bar is done loading
        if bar.done:
            # Second textbox fades in. 
            text2.Update()

            # Press space to move on to next scence
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                return
            
        # Pumping events and updating the display
        pygame.display.flip()
        pygame.event.pump() 

def ApplicationSelect():
    global screen, running
    FadedIN = False

    selector = ui.ApplicationSelector()
    BackButton = ui.Button((35,35), (50, 50), "<-")

    while running:
        clock.tick(60)
        screen.fill(background_colour)

        Text("Select an app", (350, 50))
        selector.Update()
        BackButton.Update()

        if BackButton.pressed:
            ui.FadeEffect().Update()
            return

        # Fading in
        if FadedIN == False:
            ui.FadeEffect(-1).Update()
            FadedIN = True

        # Exiting if window is x button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        pygame.display.flip()

def MainMenu():
    global screen, running

    # Ressetting everything
    screen = pygame.display.set_mode((700, 500))

    PlayMusic("MainMenu", 2)

    stonkLoader = background.Stonks()
    StartButton = ui.Button((350, 200), (200, 120), "Start")
    QuitButton = ui.Button((350, 330), (200, 120), "Quit")
    fadeOut = ui.FadeEffect()

    while running:            
        clock.tick(60)
        screen.fill(background_colour)

        stonkLoader.Update() # Updating the "stonks" background
        Text("Bored Applications", (350, 75), font="TitleFont") # Drawing title
        StartButton.Update()
        QuitButton.Update()

        # Fading out and starting a new scene if start button is pressed
        if StartButton.pressed:
            fadeOut.Update()
            ApplicationSelect()
            return

        # Fading out and exiting if the quit button is pressed
        if QuitButton.pressed:
            running = False
            ui.FadeEffect().Update()
            sys.exit()

        # Exiting if window is x button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            
            
        pygame.display.flip()

LoadingScreen()

while True:
    MainMenu()
