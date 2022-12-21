import random
import pygame

# Initializing Pygame
pygame.font.init()
pygame.init()

# Vars
background_colour = (23, 23, 23)
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
running = True
sorted = False
startSorting = False
loop = False

def GenerateNumbers():
    nums = []

    for i in range(screen.get_width()):
        nums.append(random.randint(1, screen.get_height()-100))
    return nums

nums = GenerateNumbers()

# Text Function
def Text(msg:str, position:tuple, color:tuple=(255,255,255), size:int=50):
    font = pygame.font.SysFont(None,  size)
    text = font.render(msg, True, color)

    rect = text.get_rect()

    rect.center = position

    screen.blit(text, rect)

# Actually Sorting
def Sort():
    global startSorting, sorted, nums

    if not sorted and startSorting:
        i = 0
        correctNumbers = 0

        while i < len(nums)-1:
            left = nums[i]
            right = nums[i+1]


            if left > right:
                nums[i+1] = left
                nums[i] = right 
                
            if left <= right:
                correctNumbers +=1
            
            if correctNumbers == len(nums)-1:
                sorted = True
            i +=1

def ShowStatus():
    global startSorting, sorted
    if loop:
        return
        
    if not startSorting:
        Text("Press enter to starting sorting", (screen.get_width()/2, 50))
    elif startSorting and not sorted:
        Text("Sorting..", (screen.get_width()/2, 50), color=(255, 255, 0))
    else:
        Text("Press L to loop or press escape to exit", (screen.get_width()/2, 50), color=(0, 255, 0))

# Representing the numbers
def Draw():
    for i in range(len(nums)):
        pygame.draw.rect(screen, (255,255,255), (i, screen.get_height()-nums[i], 1, nums[i]))

pygame.display.set_caption('Bubble Sorting Showcase')

# Main loop
while running:
    screen.fill(background_colour)
    Sort()
    ShowStatus()
    Draw()
            
    if loop and sorted:
            nums = GenerateNumbers()
            sorted = False
            pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not loop:
                if startSorting and sorted:
                    nums = GenerateNumbers()
                    sorted = False
                else:
                    startSorting = True

            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_l:
                loop = True
    pygame.display.flip()
