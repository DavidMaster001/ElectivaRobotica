#Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
#y un parámetro de salida (matriz).

import numpy as np
import math

# Ángulo en grados
angulo = 45
radianes = math.radians(angulo)

# Matriz de rotación en el eje X
rotacion_x_matriz = np.array([[1, 0, 0],
                              [0, math.cos(radianes), -math.sin(radianes)],
                              [0, math.sin(radianes), math.cos(radianes)]])

# Matriz de rotación en el eje Y
rotacion_y_matriz = np.array([[math.cos(radianes), 0, math.sin(radianes)],
                              [0, 1, 0],
                              [-math.sin(radianes), 0, math.cos(radianes)]])

# Matriz de rotación en el eje Z
rotacion_z_matriz = np.array([[math.cos(radianes), -math.sin(radianes), 0],
                              [math.sin(radianes), math.cos(radianes), 0],
                              [0, 0, 1]])

print("Matriz de rotación en el eje X:")
print(rotacion_x_matriz)

print("Matriz de rotación en el eje Y:")
print(rotacion_y_matriz)

print("Matriz de rotación en el eje Z:")
print(rotacion_z_matriz)   