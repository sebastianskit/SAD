import pygame
import sys

pygame.init()

#Colors
NEGRE = (0, 0, 0)
BLANC = (255, 255, 255)
VERMELL = (255, 0, 0)
VERD = (0, 255, 0)
BLAU = (0, 0, 255)

#Constants
ALTURA = 700
AMPLADA = 700

#Pantalla

pantalla = pygame.display.set_mode((ALTURA,AMPLADA))
pygame.display.set_caption("tictactoe")
pantalla.fill(VERD)
pygame.display.update()

ON = True
while ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            ON = False
    

