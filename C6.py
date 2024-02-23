import cv2
import numpy as np
import matplotlib.pyplot as plt

Suzuki = cv2.imread('logo1.png', cv2.IMREAD_GRAYSCALE)
lamborgini = cv2.imread('logo2.png', cv2.IMREAD_GRAYSCALE)

thres_suzuki = cv2.threshold(Suzuki, 240, 255, cv2.THRESH_BINARY)
thres_lamborgini = cv2.threshold(lamborgini, 240, 255, cv2.THRESH_BINARY)

contornos_suzuki = cv2.findContours(thres_suzuki, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_lamborgini = cv2.findContours(thres_lamborgini, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

coord_x_suzuki = []
coord_y_susuki = []
for contorno in contornos_suzuki:
    for punto in contorno:
        x, y = punto[0]
        coord_x_suzuki.append(x)
        coord_y_susuki.append(y)

coord_x_lamborgini = []
coord_y_lamborgini = []
for contorno in contornos_lamborgini:
    for punto in contorno:
        x, y = punto[0]
        coord_x_lamborgini.append(x)
        coord_y_lamborgini.append(y)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(coord_x_suzuki, coord_y_susuki, s=1, color='red')
plt.title('Contorno del logo de suzuki')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.subplot(1, 2, 2)
plt.scatter(coord_x_lamborgini, coord_y_lamborgini, s=1, color='blue')
plt.title('Contorno del logo de Lamborgini')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.tight_layout()
plt.show()