import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imágenes de los logos
logo1 = cv2.imread('logo1.jpg')
logo2 = cv2.imread('logo2.jpg')

# Convertir las imágenes a escala de grises
logo1_gris = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
logo2_gris = cv2.cvtColor(logo2, cv2.COLOR_BGR2GRAY)

# Umbralizar las imágenes para obtener los contornos
_, logo1_bin = cv2.threshold(logo1_gris, 127, 255, cv2.THRESH_BINARY)# todo el conjunto de pixeles que quede menos de 127 se van a convertir en color negro entre 127 y 255 son blancos
_, logo2_bin = cv2.threshold(logo2_gris, 127, 255, cv2.THRESH_BINARY)# todo el conjunto de pixeles que quede mayor a 255 se van a convertir en color gris

# Encontrar contornos en las imágenes umbralizadas
contornos_logo1, _ = cv2.findContours(logo1_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_logo2, _ = cv2.findContours(logo2_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear figuras de matplotlib para mostrar los contornos
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Mostrar el primer logo
axs[0].imshow(cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB))
axs[0].set_title('Logo 1')

# Dibujar los contornos del primer logo
for contorno in contornos_logo1:
    x, y, w, h = cv2.boundingRect(contorno)
    axs[0].plot([x, x+w, x+w, x, x], [y, y, y+h, y+h, y], 'r', linewidth=2)

# Mostrar el segundo logo
axs[1].imshow(cv2.cvtColor(logo2, cv2.COLOR_BGR2RGB))
axs[1].set_title('Logo 2')

# Dibujar los contornos del segundo logo
for contorno in contornos_logo2:
    x, y, w, h = cv2.boundingRect(contorno)
    axs[1].plot([x, x+w, x+w, x, x], [y, y, y+h, y+h, y], 'r', linewidth=2)

# Mostrar las figuras
plt.show()