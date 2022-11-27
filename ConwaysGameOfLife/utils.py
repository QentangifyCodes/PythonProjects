import pygame
pygame.init()

background_colour = (23, 23, 23)

infoObject = pygame.display.Info()
size = (900, 900)


def FindFactors(num):
    factors = []
    for i in range(1, num+1):
        if num%i == 0:
            factors.append(i)
    return factors


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

