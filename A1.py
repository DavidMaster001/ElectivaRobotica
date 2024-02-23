
#Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#vectores previamente inicializados.

import numpy as np

# Vectores inicializados
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
#Es una función de NumPy que crea un array a partir de una lista

# Suma de vectores
suma = vector_a + vector_b
print("Suma:", suma)

# Resta de vectores
resta = vector_a - vector_b
print("Resta:", resta)

# Producto punto
producto_punto = np.dot(vector_a, vector_b)
print("Producto punto:", producto_punto)
#Es una función de NumPy que calcula el producto punto entre dos arrays. 

# Producto cruz
producto_cruz = np.cross(vector_a, vector_b)
print("Producto cruz:", producto_cruz)
#Es una función de NumPy que calcula el producto cruz entre dos vectores.

# División de vectores (elemento por elemento)
division = vector_a / vector_b
print("División:", division)

