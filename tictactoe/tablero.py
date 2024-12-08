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
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

#Variables
vectorLinesList = [
    #Vertical Lines
    (WIDTH/3, 0), (WIDTH/3, HEIGHT), (WIDTH*2/3, 0), (WIDTH*2/3, HEIGHT),
    #Horizontal Lines
    (0, HEIGHT/3), (WIDTH, HEIGHT/3), (0, HEIGHT*2/3), (WIDTH, HEIGHT*2/3),
    ]

screenMatrix = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

player = "X"
gameOver = False 

#Pantalla
pygame.init()
screen = pygame.display.set_mode(SIZE)

def drawGameScreen():
    pygame.display.set_caption("tictactoe")
    screen.fill(WHITE)
    for i in range(0,len(vectorLinesList),2):
        pygame.draw.line(screen, BLACK, vectorLinesList[i], vectorLinesList[i+1])
   
def drawFigures():
    for row in range(3):
        for col in range(3):
            if screenMatrix[row][col] == "O":
                pygame.draw.circle(
                    screen,     
                    BLUE, 
                    (int(col * WIDTH/3 + WIDTH/6), int(row * HEIGHT/3 + HEIGHT/6)),
                    CIRCLE_RADIUS, 
                    CIRCLE_WIDTH
                    )
            elif screenMatrix[row][col] == "X":
                pygame.draw.line(
                    screen, 
                    RED,
                    (int(col * WIDTH/3 + SPACE), int(row * HEIGHT/3 + SPACE)),
                    (int(col * WIDTH/3 + WIDTH/3 - SPACE), int(row * HEIGHT/3 + HEIGHT/3 - SPACE)), 
                    CROSS_WIDTH
                    )
                pygame.draw.line(
                    screen, 
                    RED, 
                    (int(col * WIDTH/3 + SPACE), int(row * HEIGHT/3 + HEIGHT/3 - SPACE)),
                    (int(col * WIDTH/3 + WIDTH/3 - SPACE), int(row * HEIGHT/3 + SPACE)), 
                    CROSS_WIDTH
                    )

def checkWinner():
    #Check Rows
    for row in range(3):
        if screenMatrix[row][0] == screenMatrix[row][1] == screenMatrix[row][2] and screenMatrix[row][0] is not None:
            return screenMatrix[row][0]
    
    #Check Columns
    for col in range(3):
        if screenMatrix[0][col] == screenMatrix[1][col] == screenMatrix[2][col] and screenMatrix[0][col] is not None:
            return screenMatrix[0][col]
    
    #Check Diagonals
    if screenMatrix[0][0] == screenMatrix[1][1] == screenMatrix[2][2] and screenMatrix[0][0] is not None:
        return screenMatrix[0][0]
    if screenMatrix[0][2] == screenMatrix[1][1] == screenMatrix[2][0] and screenMatrix[0][2] is not None:
        return screenMatrix[0][2]
    else:
        return None

def isDraw():
    for row in screenMatrix:
        if None in row:
            return False
    return True

drawGameScreen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            #Coord X 
            mouseX = event.pos[0]  
            #Coord Y
            mouseY = event.pos[1]  
            
            clickedCol = mouseX/(WIDTH//3)
            clickedRow = mouseY/(HEIGHT//3)

            if screenMatrix[int(clickedRow)][int(clickedCol)] is None:
                screenMatrix[int(clickedRow)][int(clickedCol)] = player
                if checkWinner():
                    gameOver = True
                elif isDraw():
                    gameOver = True
                
                if player == "X":
                    player = "O"
                else:
                    player = "X"

        if gameOver and event.type == pygame.KEYDOWN:
            #Reset game with R
            if event.key == pygame.K_r:  
                screenMatrix = [[None, None, None],
                                [None, None, None],
                                [None, None, None]
                                ]
                player = "X"
                gameOver = False
                screen.fill(WHITE)
                drawGameScreen()

    drawFigures()
    pygame.display.update()