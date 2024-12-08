import sys
import pygame

pygame.init()

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Constants
GAME_SIZE = WIDTH, HEIGHT = 600, 600
TOTAL_SIZE = WIDTH, HEIGHT2 = 600, 700
EXTRA_SIZE = 100
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 20
CROSS_WIDTH = 25
SPACE = 50

#Variables
vectorLinesList = [
    #Vertical Lines
    (WIDTH/3, EXTRA_SIZE), (WIDTH/3, HEIGHT + EXTRA_SIZE), 
    (WIDTH * 2/3, EXTRA_SIZE), (WIDTH * 2/3, HEIGHT + EXTRA_SIZE),
    #Horizontal Lines
    (0, HEIGHT/3 + EXTRA_SIZE), (WIDTH, HEIGHT/3 + EXTRA_SIZE), 
    (0, HEIGHT * 2/3 + EXTRA_SIZE), (WIDTH, HEIGHT * 2/3 + EXTRA_SIZE),
    ]

screenMatrix = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

player = "X"
playerTurn = "Turn of X"
gameOver = False 
initScreenStatus = True

#Pantalla
screen = pygame.display.set_mode(TOTAL_SIZE)
font = pygame.font.Font(None,40)
font2 = pygame.font.Font(None,30)
title = font.render("Welcome to TicTacToe Game ", True, BLACK)
caption = font.render("Press SPACE to Play ", True, BLACK)
authors = font2.render("Arnau Ruiz and Sebastian Skit ", True, BLACK)
titleWidth = title.get_width()/2
captionWidth = caption.get_width()/2
authorsWidth = authors.get_width()/2

vectorFontList = [
    ((WIDTH//2-titleWidth,HEIGHT/6)),  #Title
    ((WIDTH//2-captionWidth,HEIGHT/3)),  #Caption
    ((WIDTH//2-authorsWidth,HEIGHT*5/6)) #Authors
    ]

def drawInitScreen():
    pygame.display.set_caption("Menu")
    screen.fill(WHITE)
    screen.blit(title,vectorFontList[0])
    screen.blit(caption,vectorFontList[1])
    screen.blit(authors,vectorFontList[2])
   

def drawGameScreen():
    pygame.display.set_caption("TicTacToe")
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, EXTRA_SIZE))
    for i in range(0,len(vectorLinesList),2):
        pygame.draw.line(screen, BLACK, vectorLinesList[i], vectorLinesList[i+1])
   
def drawFigures():
    for row in range(3):
        for col in range(3):
            if screenMatrix[row][col] == "O":
                pygame.draw.circle(
                    screen,     
                    BLUE, 
                    (int(col * WIDTH/3 + WIDTH/6), int(row * HEIGHT/3 + HEIGHT/6 + EXTRA_SIZE)),
                    CIRCLE_RADIUS, 
                    CIRCLE_WIDTH
                    )
            elif screenMatrix[row][col] == "X":
                pygame.draw.line(
                    screen, 
                    RED,
                    (int(col * WIDTH/3 + SPACE), int(row * HEIGHT/3 + SPACE + EXTRA_SIZE)),
                    (int((col + 1) * WIDTH/3 - SPACE), int((row + 1) * HEIGHT/3 - SPACE + EXTRA_SIZE)), 
                    CROSS_WIDTH
                    )
                pygame.draw.line(
                    screen, 
                    RED, 
                    (int(col * WIDTH/3 + SPACE), int((row + 1) * HEIGHT / 3 - SPACE + EXTRA_SIZE)),
                    (int((col + 1) * WIDTH/3 - SPACE), int(row * HEIGHT/3 + SPACE + EXTRA_SIZE)), 
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

def gameReset():
    global screenMatrix, player, gameOver
    screenMatrix = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]
    player = "X"
    gameOver = False
    screen.fill(WHITE)
    drawGameScreen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if initScreenStatus:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                initScreenStatus = False
                drawGameScreen()
                
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                #Coord X 
                mouseX = event.pos[0]  
                #Coord Y
                mouseY = event.pos[1] - EXTRA_SIZE
                if mouseY >= 0 and mouseY < HEIGHT:
                    clickedCol = mouseX//(WIDTH//3)
                    clickedRow = mouseY//(HEIGHT//3)
                    
                    if screenMatrix[clickedRow][clickedCol] is None: 
                        screenMatrix[clickedRow][clickedCol] = player
                        
                        if checkWinner():
                            gameOver = True
                        elif isDraw():
                            gameOver = True
                    
                        if player == "X":
                            player = "O"
                        else:
                            player = "X"

            if gameOver and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameReset()

    if initScreenStatus:
        drawInitScreen()
    else:
        drawGameScreen()
        drawFigures()
    pygame.display.update()