import sys
import pygame


#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Constants
SIZE = WIDTH, HEIGHT = 700,700

#Variables
vectorLinesList = [
    #Vertical Lines
    (WIDTH/3, 0), (WIDTH/3, HEIGHT), (WIDTH*2/3, 0), (WIDTH*2/3, HEIGHT),
    #Horizontal Lines
    (0, HEIGHT/3), (WIDTH, HEIGHT/3), (0, HEIGHT*2/3), (WIDTH, HEIGHT*2/3)
    ]

screenMatrix = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

#Pantalla
pygame.init()

def drawGameScreen():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("tictactoe")
    screen.fill(WHITE)
    for i in range(0,len(vectorLinesList),2):
        pygame.draw.line(screen, BLACK, vectorLinesList[i], vectorLinesList[i+1])
   
def drawFigures():
    for row in range(3):
        for col in range(3):
            if screenMatrix[row][col] == "O":
                pygame.draw.circle(screen, BLUE, (350,350), 20, 20)

drawGameScreen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()