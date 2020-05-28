#Librerias necesarias
import pygame
import numpy as np

#Declaramos inicio de ventana
pygame.init()
#Ancho y Largo de Pantalla
width, height = 1000,1000
#Creacion de la pantalla
screen = pygame.display.set_mode((height,width))
# Color de fondo Casi oscuro, Casi Negro
bd = 25, 25 ,25
#Pintamos la pantalla con color elegido
screen.fill(bd)

nxC, nyC = 25, 25

dimCW = width  / nxC
dimCH = height / nyC

#Estado de las celdas 1:Vivas, 0:Muertas 
gamestate = np.zeros((nxC,nyC))

#Bucle del juego
while True:

    for y in range(0, nxC):
        for x in range(0, nyC):

            poly = [( x   * dimCW, y   * dimCH),
                    ((x+1)* dimCW, y   * dimCH),
                    ((x+1)* dimCW,(y+1)* dimCH),
                    ( x   * dimCW,(y+1)* dimCH)                 
                    ]
            pygame.draw.polygon(screen, (128,128,128), poly, 1)

    pygame.display.flip()











