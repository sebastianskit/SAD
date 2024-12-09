import sys
import pygame

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensions
WIDTH, HEIGHT = 600, 600
EXTRA_SIZE = 100
HEIGHT2 = HEIGHT + EXTRA_SIZE
TOTAL_SIZE = WIDTH, HEIGHT2
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 20
CROSS_WIDTH = 25
SPACE = 50

# Display line coordinates
vectorLinesList = [
    #Vertical Lines
    (WIDTH/3, EXTRA_SIZE), (WIDTH/3, HEIGHT + EXTRA_SIZE), 
    (WIDTH * 2/3, EXTRA_SIZE), (WIDTH * 2/3, HEIGHT + EXTRA_SIZE),
    #Horizontal Lines
    (0, HEIGHT/3 + EXTRA_SIZE), (WIDTH, HEIGHT/3 + EXTRA_SIZE), 
    (0, HEIGHT * 2/3 + EXTRA_SIZE), (WIDTH, HEIGHT * 2/3 + EXTRA_SIZE),
    ]

# Variables
screenMatrix = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

# States
player = "X"
gameOver = False 
initScreenStatus = True
gameScreenStatus = False

# Screen setup
screen = pygame.display.set_mode(TOTAL_SIZE)
font = pygame.font.Font(None,40)
font2 = pygame.font.Font(None,30)
font3 = pygame.font.Font(None,80)

# Sounds
clickSounds = {
    "O": pygame.mixer.Sound("tictactoe/sounds/click.mp3"),
    "X": pygame.mixer.Sound("tictactoe/sounds/click2.mp3"),
}
winSound = pygame.mixer.Sound("tictactoe/sounds/victory.mp3")
drawSound = pygame.mixer.Sound("tictactoe/sounds/draw.mp3")
errorSound = pygame.mixer.Sound("tictactoe/sounds/error.mp3")

# Display texts
texts = {
    "title": font.render("Welcome to TicTacToe Game ", True, BLACK),
    "caption": font.render("Press SPACE to Play ", True, BLACK),
    "authors": font2.render("Arnau Ruiz and Sebastian Skit ", True, BLACK),
    "turn": font.render(f"Turn of {player} !", True, WHITE),
    "reset": font2.render("Press R to Restart", True, WHITE),
}

# Display texts coordinates
vectorFontList = [
    ((WIDTH//2 - texts["title"].get_width()/2, HEIGHT/6)),     #Title
    ((WIDTH//2 - texts["caption"].get_width()/2, HEIGHT/3)),   #Caption
    ((WIDTH//2 - texts["authors"].get_width()/2, HEIGHT * 5/6)), #Authors
    ((WIDTH//2 - texts["turn"].get_width()/2, EXTRA_SIZE/3)),  #Turn
    ((WIDTH//2 - texts["reset"].get_width()/2, HEIGHT2 * 2/3))
    ]

def drawInitScreen():
    """
    Draws the initial screen of the Tic Tac Toe game.

    Description
    -----------
    This function sets up the menu screen for the game.
    It displays the title, the caption and authors names centered
    on a white screen.
    
    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    The initial screen acts as the entry point for the game,
    requiring the player to press the SPACE key to continue.

    """
    pygame.display.set_caption("Menu")
    screen.fill(WHITE)
    screen.blit(texts["title"], vectorFontList[0])
    screen.blit(texts["caption"], vectorFontList[1])
    screen.blit(texts["authors"], vectorFontList[2])
    
def drawGameScreen():
    """
    Draws the main screen of the Tic Tac Toe game.

    Description
    -----------
    This function initializes the playing screen with a white background,
    a black header for turn status, and the game grid lines.
    It sets up the interface for players to make their moves.
    
    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    This function uses predefined line positions to draw the game grid,
    and displays the current player turn.

    """
    screen.fill(WHITE)
    pygame.display.set_caption("TicTacToe")
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, EXTRA_SIZE))
    screen.blit(texts["turn"],vectorFontList[3])
    for i in range(0,len(vectorLinesList),2):
        pygame.draw.line(screen, BLACK, vectorLinesList[i], vectorLinesList[i+1])


def drawEndScreen(winner):
    """
    Draws the end screen of the Tic Tac Toe game to display 
    the game's result.

    Description
    -----------
    This function displays the game's result on the screen based on the winner.
    If a player wins, the screen will indicate the winner.
    If the game is a draw, it will show a draw message.
    
    Parameters
    ----------
    winner: str or None
        The symbol of the winning player ("X" or "O") if there is a winner,
        or None if the game ends in a draw.

    Returns
    -------
    None

    Notes
    -----
    The end screen includes a reset prompt for restarting the game,
    allowing players to press "R" to play again.

    """
    screen.fill(BLACK)
    screen.blit(texts["reset"],vectorFontList[4])
    if winner == "O":
        endText = font3.render("O wins!", True, BLUE)
    elif winner == "X":
        endText = font3.render("X wins!", True, RED)
    else:
        endText = font3.render("It's a draw!", True, WHITE)
    screen.blit(endText,((WIDTH//2 - endText.get_width()/2, HEIGHT2 * 1/3)))
        

def drawFigures():
    """
    Draws the X and O symbols on the game grid based on the current state.

    Description
    -----------
    This function iterates through the 'screenMatrix' and draws 
    the corresponding shapes (circle for "O", cross for "X") in the grid 
    cells where a player has made a move.
    
    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    Circles are drawn for player "O" in blue, while crosses are drawn 
    for player "X" in red. Both shapes are positioned within their respective 
    grid cells.

    """
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
    """
    Check if there is a winner in the current state of the game.

    Description
    -----------
    This function evaluates the `screenMatrix` to determine if any player 
    (X or O) has met the winning conditions. Winning conditions include 
    three consecutive marks in a row, column, or diagonal.
    
    Parameters
    ----------
    None

    Returns
    -------
    str or None
        The symbol of the winning player ("X" or "O") if a winner is found, 
        or None if there is no winner yet.

    Notes
    -----
    The function checks all rows, columns, and both diagonals for a winning 
    pattern. If a match is found, it immediately returns the winner's symbol.

    """
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
    """
    Check if the game has ended in a draw.

    Description
    -----------
    This function evaluates the `screenMatrix` to determine if all cells 
    are filled and no player has won, which indicates a draw.
    
    Parameters
    ----------
    None

    Returns
    -------
    bool
        True if the game is a draw, False otherwise.

    Notes
    -----
    The function checks for empty cells in the `screenMatrix`. 
    If none are found and there is no winner, it concludes the game 
    as a draw.

    """
    for row in screenMatrix:
        if None in row:
            return False
    return True

def gameReset():
    """
    Resets the game to its game screen state.
    
    Description
    -----------
    This function clears the `screenMatrix`, resets the player turn to "X", 
    and reinitializes all game-related variables. It also redraws the 
    game screen to start a new round.

    Parameters
    ----------
    None

    Returns
    -------
    str or None
        The symbol of the winning player ("X" or "O") if a winner is found, 
        or None if there is no winner yet.

    Notes
    -----
    After resetting, the game immediately enters the playing state 
    and displays the updated game screen.

    """
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
    winSound.stop()
    drawSound.stop()
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
                        clickSounds[player].play()
                        winner = checkWinner()
                        if winner:
                            gameScreenStatus = False
                            gameOver = True
                            winSound.play(loops = -1)
                            drawEndScreen(winner)   
                        elif isDraw():
                            gameScreenStatus = False
                            gameOver = True
                            drawEndScreen(None)
                        else:
                            player = "O" if player == "X" else "X"
                            texts["turn"] = font.render(f"Turn of {player} !", True, WHITE)
                    else:
                        errorSound.play()
            if gameOver and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameReset()
                    
    # Draws screen based on the current state
    if initScreenStatus:
        drawInitScreen()
    elif gameScreenStatus:
        drawGameScreen()
        drawFigures()
        
    pygame.display.update()