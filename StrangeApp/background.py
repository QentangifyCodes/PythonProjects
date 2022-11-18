from screen import *
import random

# Stock Market Share Price Meme thing
class Stonks:
    def __init__(self):
        self.stonks = []

        # How many squares the newest stonk has
        self.currentStonkSize = 0
        # How many squares the last stonk. Used for stonk colors
        self.lastStonkSize = 0

        # The time until a new stonk is created. Between 0-1
        self.timeTillNextStonk = 0

    def Draw(self):
        for stonk in self.stonks:
            # Drawing each square in a stonk
            for square in stonk:
                # Determining color based of if the current stonk is greater or less than the previous 
                color = (255,255,0)
                if self.lastStonkSize < self.currentStonkSize:
                    color = (0,255,0)
                elif self.lastStonkSize > self.currentStonkSize:
                    color = (255,0,0)

                pygame.draw.rect(screen, color, square)

    def CreateStonk(self):
        # Moving all current stonks left
        for x in range(len(self.stonks)):
            for y in range(len(self.stonks[x])):
                square = self.stonks[x][y] 
                square.topleft = (square.topleft[0]-35, square.topleft[1])

                # Removing a stonk that goes off screen
                if square.topleft[0]<0:
                    self.stonks.remove(self.stonks[x])
                    return                

                self.stonks[x][y]=square

        stonk = []

        # Resetting the last and current stonk sizes
        self.lastStonkSize = self.currentStonkSize
        self.currentStonkSize  = 0

        # Generating a random number of squares for the stonk to have
        for x in range(random.randint(1, 11)):
            stonk.append(pygame.Rect(675, 475-(x*35), 25, 25))
            self.currentStonkSize +=1
        self.stonks.append(stonk)
    
    def Update(self):
        self.Draw()

        # Creating a new stonk every couple frames
        if self.timeTillNextStonk<1:
            self.timeTillNextStonk+=0.01
        else:
            self.timeTillNextStonk = 0
            self.CreateStonk()

class DotBackground():
    def __init__(self):
        self.positions = []

        # Drawing one extra row of dots to move them seamlessly 
        x,y = 20, -40
        while x < 700:
            while y < 500:
                self.positions.append([x, y])
                y+= 50
            
            x+= 50
            y = -40

    def Draw(self):
        for position in self.positions:
            pygame.draw.circle(screen, (50, 50, 50), (position), 5)

    def Update(self):
        self.Draw()

        # Moving each dot. Moving to the top if it goes off screen
        for i in range(len(self.positions)):
            self.positions[i][1]+=2

            if self.positions[i][1]>500:
                self.positions[i][1] = -40

class FakeLoadingBar:
    def __init__(self):
        self.size = 10
        self.done = False
    
    def Draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (10, 470, int(self.size), 20))
    
    def Update(self):
        self.Draw()
        
        # Increasing size until it almost goes offscreen
        if self.size >= 670:
            self.done = True    
        else:
            self.size += random.gauss(10, 5) # Adding a "guass" number. A random number but close to 10
