import entity
import pygame

class Tile(entity.Sprite):
    def __init__(self, window, position: tuple, size:int, sprite: str = None):
        super().__init__(window, position, sprite)
        self.size = size
        self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))
        self.sprite.set_alpha(30)
# Any Drawable Entity
class Grid(entity.Entity):
    def __init__(self, window):
        self.window = window
        self.cells = []
        self.cellSize = 0

        for i in range(50, 0, -1):
            if self.window.size.x%i != 0:
                continue
            self.cellSize = i
            break
        
        print(self.cellSize, self.window.size)
        for y in range(0, int(self.window.size.y), self.cellSize):
            for x in range(0, int(self.window.size.x), self.cellSize):   
                self.cells.append(Tile(self.window, (x,y), self.cellSize, "Assets/Tile.png"))

    
        super().__init__()

    def Update(self):
        for cell in self.cells:
            cell.Update()
