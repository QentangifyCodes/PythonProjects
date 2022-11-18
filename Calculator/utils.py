import pygame
pygame.font.init()


background_color = (38, 102, 207)
pygame.display.set_caption('Calculator')
pygame.display.set_icon(pygame.image.load("logo.png"))
screen = pygame.display.set_mode((400, 300))

def DrawText(text: str, position: tuple, size: int = 50):
    font = pygame.font.SysFont('sans-serif', size)
    text = font.render(text, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = position

    screen.blit(text, textRect)
