import pygame, sys

pygame.init()
pygame.font.init()
pygame.mixer.init()

background_colour = (23, 23, 23)
running = True

screen = pygame.display.set_mode((700, 500), pygame.NOFRAME)
clock = pygame.time.Clock()
pygame.display.set_caption('Bored Applications™')

def PlayMusic(music:str, volume:float=50):
    pygame.mixer.music.load(f"Assets/Music/{music}.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

def Text(msg:str, position:tuple, color:tuple=(255,255,255), size:int=50, font:str="Font", anchor:str="center", alpha:int=250, render:bool=True):
    font = pygame.font.Font(f"Assets/Fonts/{font}.ttf", size)
    text = font.render(msg, True, color)

    text.set_alpha(alpha)

    rect = text.get_rect()

    if anchor == "center":
        rect.center = position
    elif anchor == "left":
        rect.topleft = position
    
    if render:
        screen.blit(text, rect)
    return rect

