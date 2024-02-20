#Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
#y un parámetro de salida (matriz).

import numpy as np
import math

# Función para la rotación en el eje X
def rotacion_x(angulo):
    radianes = math.radians(angulo)
    return np.array([[1, 0, 0],
                     [0, math.cos(radianes), -math.sin(radianes)],
                     [0, math.sin(radianes), math.cos(radianes)]])

# Función para la rotación en el eje Y
def rotacion_y(angulo):
    radianes = math.radians(angulo)
    return np.array([[math.cos(radianes), 0, math.sin(radianes)],
                     [0, 1, 0],
                     [-math.sin(radianes), 0, math.cos(radianes)]])

# Función para la rotación en el eje Z
def rotacion_z(angulo):
    radianes = math.radians(angulo)
    return np.array([[math.cos(radianes), -math.sin(radianes), 0],
                     [math.sin(radianes), math.cos(radianes), 0],
                     [0, 0, 1]])

# Ejemplo de uso
angulo = 45
rotacion_x_matriz = rotacion_x(angulo)
rotacion_y_matriz = rotacion_y(angulo)
rotacion_z_matriz = rotacion_z(angulo)

print("Matriz de rotación en el eje X:")
print(rotacion_x_matriz)

print("Matriz de rotación en el eje Y:")
print(rotacion_y_matriz)

print("Matriz de rotación en el eje Z:")
print(rotacion_z_matriz)
