#Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#matrices previamente inicializadas.

import numpy as np

# Matrices inicializadas
matriz_a = np.array([[9, 2], [7, 11]])
matriz_b = np.array([[9, 12], [7, -2]])

# Suma de matrices
suma = matriz_a + matriz_b
print("Suma:")
print(suma)

# Resta de matrices
resta = matriz_a - matriz_b
print("Resta:")
print(resta)

# Producto punto de matrices 
producto_punto = matriz_a * matriz_b
print("Producto punto:")
print(producto_punto)

# Producto cruz de matrices 
producto_cruz = np.dot(matriz_a, matriz_b)
print("Producto cruz:")
print(producto_cruz)

# División de matrices
division = matriz_a / matriz_b
print("División:")
print(division)


