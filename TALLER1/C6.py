import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer las imágenes en escala de grises
Renault = cv2.imread('logo1.png', cv2.IMREAD_GRAYSCALE)
hyundai = cv2.imread('logo2.png', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización para obtener imágenes binarias
_, thres_Renault = cv2.threshold(Renault, 240, 255, cv2.THRESH_BINARY)
_, thres_hyundai = cv2.threshold(hyundai, 240, 255, cv2.THRESH_BINARY)# Encontrar los contornos en las imágenes binarias

contornos_Renault, _ = cv2.findContours(thres_Renault, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_hyundai, _ = cv2.findContours(thres_hyundai, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear listas para almacenar las coordenadas de los puntos de los contornos
coord_x_Renault = []
coord_y_Renault = []
for contorno in contornos_Renault:
    for punto in contorno:
        x, y = punto[0]
        coord_x_Renault.append(x)
        coord_y_Renault.append(y)

coord_x_hyundai = []
coord_y_hyundai = []
for contorno in contornos_hyundai:
    for punto in contorno:
        x, y = punto[0]
        coord_x_hyundai.append(x)
        coord_y_hyundai.append(y)

# Crear un gráfico de dispersión para visualizar los contornos
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(coord_x_Renault, coord_y_Renault, s=1, color='b')
plt.title('Contorno del logo de Renault')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.subplot(1, 2, 2)
plt.scatter(coord_x_hyundai, coord_y_hyundai, s=1, color='b')
plt.title('Contorno del logo de hyundai')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.tight_layout()
plt.show()
