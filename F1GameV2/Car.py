import random

import pygame

import Data


class RaceCar:
    def __init__(self, screen: pygame.Surface, number: int):
        if number > 7:
            del self
            return

        self.screen = screen
        self.name = Data.DRIVER_NAMES[number]
        self.number = number

        self.team = Data.TEAMS[number]
        self.teamLogo = pygame.transform.scale(pygame.image.load("Logos/"+self.team+"-logos.jpeg"), (500, 500))

        self.skill = random.randint(50, 65) + (random.randrange(-1, 1, 2) * number)

        self.speedRange = [5, 10 + self.skill * 0.5]
        self.currentSpeed = random.uniform(self.speedRange[0], self.speedRange[1])
        self.canMove = True
        self.xCoordBeforeSpeedChange = 10

        self.points = 0
        self.wins = 0
        self.momentum = 0
        self.lastPlacement = 0

        self.position = pygame.Vector2(10, 50 + 90 * number)
        self.sprite = pygame.image.load(f"Cars/car ({number}).png")
        self.rect = self.sprite.get_rect()

    def GetNewSpeed(self):
        self.currentSpeed = random.uniform(self.speedRange[0], self.speedRange[1])+random.randint(0, 5)

    def Draw(self):
        self.rect.topleft = (int(self.position.x), self.position.y)
        self.screen.blit(self.sprite, self.rect)

    def Movement(self):
        if self.position.x + self.rect.width >= 1000:
            self.canMove = False
            return

        self.position.x += self.currentSpeed / 5

        if self.position.x - self.xCoordBeforeSpeedChange >= 100:
            self.xCoordBeforeSpeedChange = self.position.x
            self.GetNewSpeed()

    def RaceEnd(self, placement: int):
        self.points += 100 - ((placement - 1) * 10)
        self.lastPlacement = placement
        self.skill += (7-placement)
        self.speedRange = [random.randint(1,10)+self.skill, random.randint(20,30) + self.skill]

        if placement == 1:
            self.wins += 1

        if self.lastPlacement == 0:
            self.momentum = placement - self.lastPlacement

    def Update(self):
        if self.canMove:
            self.Movement()
        self.Draw()
