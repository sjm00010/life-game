# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:55:10 2020

@author: Sergio Jiménez Moreno
"""

import pygame
import numpy as np
import time

# Inicializo la pantalla
pygame.init()

# Nombre de la ventana
pygame.display.set_caption("Life Game")

# Establezco las dimensiones de la ventana
width, heigth = 800, 800 # Ancho y alto
ventana = pygame.display.set_mode((width, heigth))

# Establezco el color de fondo de la pantalla
ventana.fill((25, 25, 25))

# GRID(Cuadrícula) de la ventana
nxC, nyC = 50, 50 # Alto y ancho del Grid
dimCW = width  / nxC
dimCH = heigth / nyC

# EEDD para almacenar el juego. Viva = 1, Muerta = 0
estado = np.zeros((nxC, nyC))

# Creo un autómata de partida
estado[21, 21] = 1
estado[22, 22] = 1
estado[22, 23] = 1
estado[21, 23] = 1
estado[20, 23] = 1

# Variable para pausar el juego
pausa = False


# Bucle para visulización continua
while True:
    
    # Copio el estado actual, para que los cambios se hagan por periodo
    nuevoEstado = np.copy(estado)
    
    # Limpio la ventana
    ventana.fill((25, 25, 25))
    
    # Descanso para no saturar el sistema
    time.sleep(0.1)
    
    # Registro eventos de teclado
    evs = pygame.event.get()
    for evento in evs:
        if evento.type == pygame.KEYDOWN:
            pausa = not pausa
            
            # Finalización del juego
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
    
        # Registro eventos de ratón
        click = pygame.mouse.get_pressed()
        if sum(click) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            nuevoEstado[celX, celY] = not click[2]
    
    # Bucles para recorrer el GRID
    for y in range(0, nxC):
        for x in range(0, nyC):
            
            # Pausa
            if not pausa:
            
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
                    nuevoEstado[x, y] = 1
                
                # Regla 2: Una celula viva con menos de 2 o mas de 3 vecinos vivos "muere".
                elif estado[x, y] == 1 and (n_vecinos < 2 or n_vecinos > 3):
                    nuevoEstado[x, y] = 0
            
            # Calculo la celda, polígono a dibujar
            celda = [((x)     * dimCW,  y      * dimCH),
                     ((x + 1) * dimCW,  y      * dimCH),
                     ((x + 1) * dimCW, (y + 1) * dimCH),
                     ((x)     * dimCW, (y + 1) * dimCH)]
            
            # Dibujo la cuadrícula (GRID)
            if nuevoEstado[x, y] == 0:
                # La función de necesita (ventana, color de fondo, celdas, grosor línea)
                pygame.draw.polygon(ventana, (128,128,128), celda, 1)
            else:
                pygame.draw.polygon(ventana, (255,255,255), celda, 0)
    
    # Actualizo el estado
    estado = np.copy(nuevoEstado)
    
    # Muestro y acualizo el GRID
    pygame.display.flip()