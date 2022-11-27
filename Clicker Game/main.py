from screen import *
import blob
import rain
b = blob.Blob()
background = rain.RainBackground()

while running:
    clock.tick(60)
    screen.fill(background_colour)
    background.Update()
    b.Update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            b.Click()
    pygame.display.flip()
