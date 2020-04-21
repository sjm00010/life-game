# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:55:10 2020

@author: Sergio Jiménez Moreno
"""

import pygame
import numpy as np

# Inicializo la pantalla
pygame.init()

# Nombre de la ventana
pygame.display.set_caption("Life Game")

# Establezco las dimensiones de la ventana
width, heigth = 1000, 1000 # Ancho y alto
ventana = pygame.display.set_mode((width, heigth))

# Establezco el color de fondo de la pantalla
ventana.fill(25 , 25, 25)

# GRID(Cuadrícula) de la ventana
nxC, nyC = 25, 25 # Alto y ancho del Grid
dimCW = width  / nxC
dimCH = heigth / nyC

# EEDD para almacenar el juego. Viva = 1, Muerta = 0
estado = np.zeros((nxC, nyC))

# Bucle para visulización continua
while True:
    
    # Bucles para recorrer el GRID
    for y in range(0, nxC):
        for x in range(0, nyC):
            
            # Calculo el número de vecinos cercanos
            n_vecinos = estado[(x - 1) % nxC, (y - 1) % nyC] + \
                        estado[(x)     % nxC, (y - 1) % nyC] + \
                        estado[(x + 1) % nxC, (y - 1) % nyC] + \
                        estado[(x - 1) % nxC, (y)     % nyC] + \
                        estado[(x + 1) % nxC, (y)     % nyC] + \
                        estado[(x - 1) % nxC, (y + 1) % nyC] + \
                        estado[(x)     % nxC, (y + 1) % nyC] + \
                        estado[(x + 1) % nxC, (y + 1) % nyC]
            
            # Regla 1: Una celula muerta con 3 vecinos vivos "revive".
            if estado[x, y] == 0 and n_vecinos == 3:
                estado[x, y] = 1
            
            # Regla 2: Una celula viva con menos de 2 o mas de 3 vecinos vivos "muere".
        elif estado[x, y] == 1 and (n_vecinos < 2 or n_vecinos > 3):
            estado[x, y] = 0
            
            # Calculo la celda
            celda = [((x)     * dimCW,  y      * dimCH),
                     ((x + 1) * dimCW,  y      * dimCH),
                     ((x + 1) * dimCW, (y + 1) * dimCH),
                     ((x)     * dimCW, (y + 1) * dimCH)]
            
            # Dibujo la cuadrícula (GRID)
            # La función de necesita (ventana, color de fondo, celdas, grosor línea)
            pygame.draw.polygon(ventana, (128,128,128), celda, 1)
    
    # Muestro y acualizo el GRID
    pygame.display.flip()
    
    
    