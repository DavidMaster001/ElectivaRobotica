#Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
#y un parámetro de salida (matriz).

import numpy as np
import math

def rotacion_x(angulo):
    radianes = math.radians(angulo)
    matriz = np.array([[1, 0, 0],
                       [0, math.cos(radianes), -math.sin(radianes)],
                       [0, math.sin(radianes), math.cos(radianes)]])
    return matriz

def rotacion_y(angulo):
    radianes = math.radians(angulo)
    matriz = np.array([[math.cos(radianes), 0, math.sin(radianes)],
                       [0, 1, 0],
                       [-math.sin(radianes), 0, math.cos(radianes)]])
    return matriz

def rotacion_z(angulo):
    radianes = math.radians(angulo)
    matriz = np.array([[math.cos(radianes), -math.sin(radianes), 0],
                       [math.sin(radianes), math.cos(radianes), 0],
                       [0, 0, 1]])
    return matriz

# Ejemplo de uso:
angulo = 45

matriz_rotacion_x = rotacion_x(angulo)
matriz_rotacion_y = rotacion_y(angulo)
matriz_rotacion_z = rotacion_z(angulo)

print("Matriz de rotación en el eje X:")
print(matriz_rotacion_x)

print("Matriz de rotación en el eje Y:")
print(matriz_rotacion_y)

print("Matriz de rotación en el eje Z:")
print(matriz_rotacion_z)
