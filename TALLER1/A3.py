#Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual
#deben consultar sobre el uso de funciones trigonométricas en Python.

import math

# Funciones trigonométricas en Python
# Para calcular seno, coseno y tangente de un ángulo en radianes
# angulo = math.pi / 4  # Ángulo de 45 grados en radianes
# seno = math.sin(angulo)
# coseno = math.cos(angulo)
# tangente = math.tan(angulo)

# Para convertir coordenadas rectangulares a cilíndricas y esféricas
x = 1
y = 1
z = 1

# Coordenadas cilíndricas
r = math.sqrt(x**2 + y**2)  # Radio en el plano xy se usa doble asterisco para elevar la expresión
theta = math.atan2(y, x)    # Ángulo con respecto al eje x

# Coordenadas esféricas
rho = math.sqrt(x**2 + y**2 + z**2)  # Distancia al origen
phi = math.atan2(math.sqrt(x**2 + y**2), z)  # Ángulo con respecto al eje z
theta = math.atan2(y, x)  # Ángulo en el plano xy

# Imprimir resultados
# print("Seno:", seno)
# print("Coseno:", coseno)
# print("Tangente:", tangente)
print("Coordenadas cilíndricas (r, theta):", r, theta)
print("Coordenadas esféricas (rho, phi, theta):", rho, phi, theta)
