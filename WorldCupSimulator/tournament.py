from gameobject import Gameobject
import pygame, random

class Tournament(Gameobject):
    def __init__(self, scene, teams:list):
        super().__init__(scene)
        self.teams = teams
        self.fixtures = []
        self.winners = []

        self.rounds = 0
        self.waitTime = 1
        self.currentMatch = 0
        m = self.teams

        while len(m)>0:
            m1 = m[random.randint(0, len(m)-1)]
            m.remove(m1)
            m2 = m[random.randint(0, len(m)-1)]
            m.remove(m2)

            self.fixtures.append([m1, m2])
        
        self.show = True

    def nextMatch(self):
        self.currentMatch += 1
        
        if self.currentMatch > len(self.fixtures)-1:
            o = self.fixtures
            self.fixtures = []

            for i in range(0, len(o), 2):
                winner = self.winners[i]
                winner2 = self.winners[i+1]
                self.fixtures.append([o[i][winner].replace(" >", ""), o[i+1][winner2].replace(" >", "")])
            
            self.currentMatch = 0
            self.rounds +=1

            if self.rounds > 3:
                exit()

    def Draw(self):
        self.scene.window.Text("World Cup Simulator 2024", (self.scene.window.size.x/2, 40), size=20)
        x = 20+230*self.rounds
        y = 100

        for f in self.fixtures:
            rect = pygame.Rect(x, y, 100, 50)
            pygame.draw.rect(self.scene.window.screen, (10,10,10), rect)
            self.scene.window.Text(f[0], rect.center, size=15)
            rect2 = pygame.Rect(x+110, y, 100, 50)
            pygame.draw.rect(self.scene.window.screen, (10,10,10), rect2,)
            self.scene.window.Text(f[1], rect2.center, size=15)
            y+=60

        self.scene.window.Text(f"Starting next match soon", (self.scene.window.size.x/2, self.scene.window.size.y-30), size=20)

    
    def CurrentFixture(self):
        return self.fixtures[self.currentMatch]

    def getWinner(self, team):
        self.fixtures[self.currentMatch][team] += " >"
        self.winners.append(team)

    def Update(self):
        if not self.show:
            return
        self.waitTime -= 0.01
        self.Draw()

        if self.waitTime <= 0:
            self.show = False
            self.waitTime = 1

        return super().Update()

class Match(Gameobject):
    def __init__(self, scene):
        super().__init__(scene)
        self.scene = scene
        self.bg = (240, 240, 240)
        self.rect = pygame.Rect(0,0, self.scene.window.size.x, self.scene.window.size.y)
        self.setup = False

    def Setup(self, team1, team2):
        if self.setup:
            return
        
        self.setup = True
        self.team1 = team1
        self.team2 = team2
        self.score = [0, 0]
        self.minutes = 0

        self.goals1 = []
        self.goals2 = []
        self.timeTillnextMinute = 1

        self.done = False
        self.winner = 0

    def Draw(self):
        pygame.draw.rect(self.scene.window.screen, self.bg, self.rect)
        self.scene.window.Text(f"{self.team1} V.S {self.team2}", (self.scene.window.size.x/2, 100), size=40, color=(0,0,0))
        self.scene.window.Text(self.team1, (100, 300), size=30, color=(0,0,0))
        self.scene.window.Text(self.team2, (self.scene.window.size.x-100, 300),  size=30, color=(0,0,0))
        self.scene.window.Text(f"{self.score[0]} - {self.score[1]}", (self.scene.window.size.x/2, 300),  size=40, color=(0,0,0))
        self.scene.window.Text(f"{self.minutes}'", (self.scene.window.size.x/2, 340),  size=30, color=(0,0,0))

        y = 330
        for goal in self.goals1:
            self.scene.window.Text(f"- Goal {goal}'", (100, y), size=15, color=(0,0,0))
            y+=30

        y = 330
        for goal in self.goals2:
            self.scene.window.Text(f"- Goal {goal}'", (self.scene.window.size.x-100, y), size=15, color=(0,0,0))
            y+=30

    def Goal(self, team):
        self.score[team-1] +=1

        if team==1:
            self.goals1.append(self.minutes)   
        else:
            self.goals2.append(self.minutes)   

    def Update(self):
        super().Update()

        if self.done:
            return

        self.timeTillnextMinute -= 0.1

        if self.timeTillnextMinute <= 0:
            self.timeTillnextMinute = 1
            self.minutes += 1

            if random.randint(0, 100)>97:
                if random.randint(0, 100)>50:
                    self.Goal(1)
                else:
                    self.Goal(2)

            
            if self.minutes>91:
                self.done = True

                if self.score[0] > self.score[1]:
                    self.winner = 0
                elif self.score[0] < self.score[1]:
                    self.winner =1
            
            if self.minutes > 80 and self.score[0] == self.score[1]:
                if random.randint(0, 100)>50:
                    self.Goal(1)
                else:
                    self.Goal(2)

            if self.minutes == 45:
                self.minutes = 50

