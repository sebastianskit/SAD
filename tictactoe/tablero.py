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
gameOver = False 
initScreenStatus = True
gameScreenStatus = False

#Pantalla
screen = pygame.display.set_mode(TOTAL_SIZE)
font = pygame.font.Font(None,40)
font2 = pygame.font.Font(None,30)
font3 = pygame.font.Font(None,80)

titleText = font.render("Welcome to TicTacToe Game ", True, BLACK)
captionText = font.render("Press SPACE to Play ", True, BLACK)
authorsText = font2.render("Arnau Ruiz and Sebastian Skit ", True, BLACK)
turnText = font.render(f"Turn of {player} !", True, WHITE)
resetText = font2.render("Press R to Restart", True, WHITE)

titleWidth = titleText.get_width()/2
captionWidth = captionText.get_width()/2
authorsWidth = authorsText.get_width()/2
turnWidth = turnText.get_width()/2
resetWidth = resetText.get_width()/2

vectorFontList = [
    ((WIDTH//2 - titleWidth, HEIGHT/6)),     #Title
    ((WIDTH//2 - captionWidth, HEIGHT/3)),   #Caption
    ((WIDTH//2 - authorsWidth, HEIGHT * 5/6)), #Authors
    ((WIDTH//2 - turnWidth, EXTRA_SIZE/3)),  #Turn
    ((WIDTH//2 - resetWidth, HEIGHT2 * 2/3))
    ]

def drawInitScreen():
    pygame.display.set_caption("Menu")
    screen.fill(WHITE)
    screen.blit(titleText, vectorFontList[0])
    screen.blit(captionText, vectorFontList[1])
    screen.blit(authorsText, vectorFontList[2])
   

def drawGameScreen():
    pygame.display.set_caption("TicTacToe")
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, EXTRA_SIZE))
    screen.blit(turnText,vectorFontList[3])
    for i in range(0,len(vectorLinesList),2):
        pygame.draw.line(screen, BLACK, vectorLinesList[i], vectorLinesList[i+1])


def drawWinnerScreen(winner):
    if winner == "O":
        screen.fill(BLACK)
        winnerText = font3.render("O wins!", True, BLUE)
    elif winner == "X":
        screen.fill(BLACK)
        winnerText = font3.render("X wins!", True, RED)
    else:
        screen.fill(BLACK)
        winnerText = font3.render("It's a draw!", True, WHITE)
        
    
    winnerWidth = winnerText.get_width()/2
    screen.blit(winnerText,((WIDTH//2 - winnerWidth, HEIGHT2 * 1/3)))

    screen.blit(resetText,vectorFontList[4])
    pygame.display.update()
        

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
    
    return None

def isDraw():
    for row in screenMatrix:
        if None in row:
            return False
    return True

def gameReset():
    global screenMatrix, player, gameOver, gameScreenStatus
    screenMatrix = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]
    player = "X"
    gameOver = False
    screen.fill(WHITE)
    gameScreenStatus = True
    drawGameScreen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if initScreenStatus:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                initScreenStatus = False
                gameScreenStatus = True
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
                        winner = checkWinner()
                        if winner:
                            gameScreenStatus = False
                            gameOver = True
                            drawWinnerScreen(winner)
                        
                        elif isDraw():
                            gameScreenStatus = False
                            gameOver = True
                            drawWinnerScreen(None)
                        else:
                            player = "O" if player == "X" else "X"
                            turnText = font.render(f"Turn of {player} !", True, WHITE)
                            

            if gameOver and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameReset()
                    

    if initScreenStatus:
        drawInitScreen()
    elif gameScreenStatus:
        drawGameScreen()
        drawFigures()
    pygame.display.update()