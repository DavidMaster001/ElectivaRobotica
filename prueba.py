import matplotlib.pyplot as plt

# Crear una figura y un eje
fig, ax = plt.subplots()

# Dibujar las letras del nombre "DAVID" en mayúsculas
# Letra D
ax.plot([0, 0], [0, 1], 'b-')
ax.plot([0, 0.5], [1, 0.5], 'b-')
ax.plot([0.5, 1], [0.5, 1], 'b-')
ax.plot([1, 1], [1, 0], 'b-')

# Letra A
ax.plot([1.2, 1.4], [0, 1], 'b-')
ax.plot([1.4, 1.6], [1, 0], 'b-')
ax.plot([1.3, 1.5], [0.5, 0.5], 'b-')

# Letra V
ax.plot([1.7, 1.8], [0, 1], 'b-')
ax.plot([1.8, 1.9], [1, 0], 'b-')

# Letra I
ax.plot([2, 2], [0, 1], 'b-')

# Letra D
ax.plot([2.2, 2.2], [0, 1], 'b-')
ax.plot([2.2, 2.4], [1, 0.5], 'b-')
ax.plot([2.4, 2.2], [0.5, 0], 'b-')

# Configurar ejes y mostrar la figura
ax.axis('equal')
ax.axis('off')
plt.show()
