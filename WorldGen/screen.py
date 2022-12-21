import pygame

pygame.init()
pygame.font.init()

background_colour = (77, 154, 255)
res = (500, 500)
screen = pygame.display.set_mode(res)
running = True

pygame.display.set_caption("Cool thing")

def Text(msg:str, position:tuple, color:tuple=(255,255,255), size:int=50):
    font = pygame.font.SysFont(None, size)
    text = font.render(msg, True, color)
    rect = text.get_rect()
    rect.topleft = position

    screen.blit(text, rect)
