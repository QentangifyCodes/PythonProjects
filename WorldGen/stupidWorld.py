from screen import *
import noise
import random

class Tile:
    def __init__(self, pos, surf, type):
        self.pos = pos
        self.surface = surf
        self.type = type
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.pos

    def Draw(self):
        screen.blit(self.surface, self.rect)

class Country:
    def __init__(self):
        self.tiles = []

    def AddTile(self, tile):
        tile.surface.fill((255,0,0))
        self.tiles.append(tile)

    def Draw(self):
        for tile in self.tiles:
            tile.Draw()

class World:
    def __init__(self, size, seed):
        self.tileSize = size
        self.seed = seed
        self.unclaimedTiles = []

        self.countires = []
        self.generateStupidWorld()
        self.generateCountry()
        print("World created!")

    def generateStupidWorld(self):
        x, y = 0, 0
        scl = self.tileSize
        percentDone = 0
        while y < res[0]:
            while x < res[1]:
                surf = pygame.Surface((1,1))
                n = noise.pnoise2(x*scl, y*scl, base=self.seed)
                type = "w"

                if -0.1<n<0.1:
                    surf.fill((250, 234, 99))
                    type = "s"
                elif 0.1<n<1:
                    surf.fill((171, 219, 35))
                    type="g"
                else:
                    surf.fill((80, 218, 254))

                tile = Tile((x,y), surf, type)
                if type=="s" or type=="g":
                    self.unclaimedTiles.append(tile)
                x+=1

                percentDone+=1
                print(f"Generating World {round(percentDone/(res[0]*res[1]), 3)*100}%")
            x=0
            y+=1
    
    def generateCountry(self):
        posTiles = self.unclaimedTiles
        country = Country()

        startTile = posTiles[random.randint(0, len(posTiles)-1)]
        country.AddTile(startTile)
        size = random.randint(100, 300)
        rect = pygame.Rect(startTile.rect.x-size, startTile.rect.y-size, startTile.rect.w+size, startTile.rect.h+size)

        tilec = 0
        for tile in posTiles:
            tilec+=1
            print(f"Generating City. Tiles Checked: {round(tilec/len(self.unclaimedTiles), 3)*100}%")
            if tile.rect.colliderect(rect):
                country.AddTile(tile)
                self.unclaimedTiles.remove(tile)
                


    def Update(self):
        for tile in self.unclaimedTiles:
            tile.Draw()
        for country in self.countires:
            country.Draw()


