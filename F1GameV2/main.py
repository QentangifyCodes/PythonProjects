import pygame
import RaceManager
import Car

pygame.init()

screen = pygame.display.set_mode((1000, 680))
pygame.display.set_caption('F1 Simulation')
Clock = pygame.time.Clock()

running = True
RaceManager = RaceManager.Manager(screen)
while running:
    Clock.tick(60)
    screen.fill((23, 23, 23))
    RaceManager.Update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()