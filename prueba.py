import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer las imágenes en escala de grises
Suzuki = cv2.imread('logo1.png', cv2.IMREAD_GRAYSCALE)
lamborgini = cv2.imread('logo2.png', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización para obtener imágenes binarias
_, thres_suzuki = cv2.threshold(Suzuki, 240, 255, cv2.THRESH_BINARY)
_, thres_lamborgini = cv2.threshold(lamborgini, 240, 255, cv2.THRESH_BINARY)

# Encontrar los contornos en las imágenes binarias
contornos_suzuki, _ = cv2.findContours(thres_suzuki, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_lamborgini, _ = cv2.findContours(thres_lamborgini, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear listas para almacenar las coordenadas de los puntos de los contornos
coord_x_suzuki = []
coord_y_suzuki = []
for contorno in contornos_suzuki:
    for punto in contorno:
        x, y = punto[0]
        coord_x_suzuki.append(x)
        coord_y_suzuki.append(y)

coord_x_lamborgini = []
coord_y_lamborgini = []
for contorno in contornos_lamborgini:
    for punto in contorno:
        x, y = punto[0]
        coord_x_lamborgini.append(x)
        coord_y_lamborgini.append(y)

# Crear un gráfico de dispersión para visualizar los contornos
plt.figure(figsize=(18, 9))
plt.subplot(1, 2, 1)
plt.scatter(coord_x_suzuki, coord_y_suzuki, s=1, color='b')
plt.title('Contorno del logo de Suzuki')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.subplot(1, 2, 2)
plt.scatter(coord_x_lamborgini, coord_y_lamborgini, s=1, color='b')
plt.title('Contorno del logo de Lamborghini')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.tight_layout()
plt.show()
