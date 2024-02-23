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
_, logo1_bin = cv2.threshold(logo1_gris, 127, 255, cv2.THRESH_BINARY)
_, logo2_bin = cv2.threshold(logo2_gris, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos en las imágenes umbralizadas
contornos_logo1, _ = cv2.findContours(logo1_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_logo2, _ = cv2.findContours(logo2_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una imagen en blanco para dibujar los contornos
contornos_img1 = np.zeros_like(logo1)
contornos_img2 = np.zeros_like(logo2)

# Dibujar los contornos en las imágenes en blanco
cv2.drawContours(contornos_img1, contornos_logo1, -1, (255, 255, 255), 2)
cv2.drawContours(contornos_img2, contornos_logo2, -1, (255, 255, 255), 2)

# Mostrar las imágenes con los contornos superpuestos
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB))
axs[0].imshow(contornos_img1, alpha=0.5, cmap='gray')
axs[0].set_title('Lamborghini')
axs[0].axis('off')

axs[1].imshow(cv2.cvtColor(logo2, cv2.COLOR_BGR2RGB))
axs[1].imshow(contornos_img2, alpha=0.5, cmap='gray')
axs[1].set_title('Chevrolet')
axs[1].axis('off')

plt.show()
