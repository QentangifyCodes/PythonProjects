import time
import random
import pygame
import Car
import Data

pygame.font.init()


def DrawText(screen: pygame.Surface, text: str, position: tuple, size: int = 50):
    Font = pygame.font.SysFont(None, size)
    Text = Font.render(text, True, (255, 255, 255))
    trect = Text.get_rect()
    trect.center = position

    screen.blit(Text, trect)


class Manager:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.cars = []
        self.finishedCars = []
        self.leaderboard = []
        self.GenerateCars()
        self.currentTrack = 0

        self.raceEnded = False
        self.counter = 0

    def GenerateCars(self):
        for i in range(7):
            self.cars.append(Car.RaceCar(self.screen, i))

    def ShowLeaderBoard(self):
        self.screen.fill((23, 23, 23))
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x.points, reverse=True)

        DrawText(self.screen, self.finishedCars[0].name[0] + " wins the " + Data.CIRCUTS[self.currentTrack] + "!",
                 (300, 30), 45)
        for i in range(len(self.leaderboard)):
            self.DrawLeaderBoardPanel(self.leaderboard[i], i)

        Logo = self.finishedCars[0].teamLogo
        Rect = Logo.get_rect()
        Rect.center = (300, 300)
        self.screen.blit(Logo, Rect)

        if self.currentTrack+1 >= len(Data.CIRCUTS):
            DrawText(self.screen, "End of the season! "+self.leaderboard[0].name[0]+" is the world champion!", (300, 600), 30)
            DrawText(self.screen, "Resetting all the stats!", (300, 650))
        else:
            DrawText(self.screen, "Next race will be starting soon...", (300, 600))

        self.counter += 1

    def DrawLeaderBoardPanel(self, car: Car.RaceCar, i: int):
        pygame.draw.rect(self.screen, (40, 40, 40), (600, 10 + (95 * i), 300, 90))
        DrawText(self.screen, car.name[0] + " " + car.name[1], (750, 10 + (95 * i) + 45), 40)
        DrawText(self.screen, str(car.points), (945, 10 + (95 * i) + 45), 40)

    def UpdateCars(self):
        DrawText(self.screen, Data.CIRCUTS[self.currentTrack], (500, 20))
        for car in self.cars:
            car.Update()

            if not car.canMove and not self.finishedCars.__contains__(car):
                car.RaceEnd(len(self.finishedCars) + 2)
                self.finishedCars.append(car)

                if len(self.finishedCars) == len(self.cars):
                    self.leaderboard = self.finishedCars
                    self.cars = self.finishedCars
                    self.raceEnded = True
                    time.sleep(2)

    def Update(self):
        if not self.raceEnded:
            self.UpdateCars()
        else:
            self.ShowLeaderBoard()

            if self.counter >= 500:
                self.raceEnded = False
                self.counter = 0
            else:
                return
            for car in self.cars:
                car.position.x = 10
                car.canMove = True
            self.finishedCars = []
            self.currentTrack += 1

            if self.currentTrack > len(Data.CIRCUTS)-1:
                self.currentTrack = 0

                for car in self.cars:
                    car.points = 0
                    car.skill = random.randint(50, 65) + (random.randrange(-1, 1, 2)*car.number)

