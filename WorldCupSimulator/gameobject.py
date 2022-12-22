import pygame, random

class Gameobject:
    def __init__(self, scene):
        self.scene = scene

    def Update(self):
        self.Draw()

    def Draw(self):
        pass

