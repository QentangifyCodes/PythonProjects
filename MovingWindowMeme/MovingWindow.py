import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame._sdl2 import Window
import random

def CommandPrompt():
    print("Microsoft Windows [Version 10.0.19043.2006]\n(c) Microsoft Corporation. All rights reserved. \n\n")

    def Line(msg:str):
        msg = r"C:\Users\kesha> "+msg+" "
        return (msg)

    def LinePrint(msg:str):
        print(Line(msg))

    def LineInput(msg:str):
        input(Line(msg))

    LinePrint("pip install virus")
    while True:
        inp =  input("Proceed y/y ")
        if inp == "y":
            break
        else:
            print(f"'Your response ('{inp}') was not one of the expected responses: y, y")
    print("Collecting virus")

    loadingbar = 1

    while loadingbar<20:
        print(f"    {int(loadingbar)/20 * 100}% ({int(loadingbar)+random.randint(0,5)} tb)", end="\r")
        print(f"                                                                          ", end="\r")
        loadingbar+=0.0001

    print("     Successfully installed virus-0.0.3")
    print("You are screwed")
    input()

def MovingWindow():
    background_colour = (23, 23, 23)
    screen = pygame.display.set_mode((100, 100), pygame.NOFRAME)

    pgwindow = Window.from_display_module() #
    window_position = [0,0]
    window_direction = [1,1]

    pygame.display.set_caption('Virus')
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        screen.fill(background_colour)
        
        window_position[0] += window_direction[0]*10
        window_position[1] += window_direction[1]*10

        if window_position[0]+700>=1920:
            window_direction[0] = -1

        if window_position[0]<=0:
            window_direction[0] = 1

        if window_position[1]+500>=1080:
            window_direction[1] = -1

        if window_position[1]<=0:
            window_direction[1] = 1 

        pgwindow.position = tuple(window_position)

        pygame.display.flip()
        
CommandPrompt()
MovingWindow()