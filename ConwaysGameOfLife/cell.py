from utils import *

class Cell: 
    def __init__(self, grid, position:tuple, size):
        self.grid = grid
        self.size = size
        self.position = pygame.Vector2(position[0], position[1])
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        self.state = 0
        self.neighbors = 0

    def Draw(self):
        pygame.draw.rect(screen, (0,0,0), self.rect)

        if self.state == 0:
            pygame.draw.rect(screen, (23,23,23), (self.position.x+4, self.position.y+4, self.size-4, self.size-4))
        else:
            pygame.draw.rect(screen, (255,255,255), (self.position.x+4, self.position.y+4, self.size-4, self.size-4))
    
    def CountNeighbors(self):
        rect = pygame.Rect(self.position.x-self.size, self.position.y-self.size, self.size*3, self.size*3)
        targetCells = []
        
        for c in self.grid.cells:
            if rect.colliderect(c.rect):
                targetCells.append(c)

        targetCells.remove(self)


        livingAmt = 0
        for c in targetCells:
            if c.state == 1:
                livingAmt+=1
        
        self.neighbors = livingAmt
    def UpdateState(self):

        if self.state == 1:
            if self.neighbors > 3 or self.neighbors <2:
                self.state = 0
        if self.state ==0:
            if self.neighbors == 3:
                self.state =1
