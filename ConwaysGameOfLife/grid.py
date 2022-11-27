import cell
from utils import *

class Grid:
    def __init__(self, size):
        self.cells = []
        self.cellSize = size
        self.generations = 0
        self.tick = 1
        self.started = False
        self.GenerateGrid()
    
    def GenerateGrid(self):
        x, y = 0, 0

        while y < screen.get_height():
            while x < screen.get_width():
                c = cell.Cell(self, (x,y), self.cellSize)

                self.cells.append(c)
                x+=self.cellSize

            x = 0
            y+=self.cellSize

    def EditMode(self):
        self.Draw()
        if self.started:
            return
        
        for cell in self.cells:
            if pygame.mouse.get_pressed()[0]:
                if cell.rect.collidepoint(pygame.mouse.get_pos()):
                    cell.state = 1
            if pygame.mouse.get_pressed()[2]:
                if cell.rect.collidepoint(pygame.mouse.get_pos()):
                    cell.state = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.started = True

    def Draw(self):
        for cell in self.cells:
            cell.Draw()

    def Update(self):
        self.Draw()
        self.tick -= 0.05

        if self.tick < 0:
            for i in range(len(self.cells)):
                self.cells[i].CountNeighbors()
            for i in range(len(self.cells)):
                self.cells[i].UpdateState()
            
            self.tick = 1
            self.generations+=1