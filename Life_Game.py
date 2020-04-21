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

# Establezco las dimensiones de la pantalla
width, heigth = 1000, 1000
ventana = pygame.display.set_mode((width, heigth))

# Establezco el color de fondo de la pantalla
ventana.fill(25 , 25, 25)

# Bucle para visulización continua
while True:
    pass