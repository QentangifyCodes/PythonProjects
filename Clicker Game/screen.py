import pygame
pygame.init()
pygame.font.init()

background_colour = (23, 23, 23)
screen = pygame.display.set_mode((900, 900))
size = (screen.get_width(), screen.get_height())

pygame.display.set_caption('Game')
clock = pygame.time.Clock()

running = True

def Text(msg:str, position:tuple, color:tuple=(255,255,255), size:int=50):
    font = pygame.font.SysFont(None, size)
    text = font.render(msg, True, color)

    rect = text.get_rect()

    rect.center = position

    screen.blit(text, rect)
